"""EventBridge event buses (eventbridgev2) against real AWS: the rpcv2Cbor protocol end to end.

``TestAsyncReadOnly`` creates nothing and is free. Everything else creates an
event bus and publishes to it, so it is paid; a bus left behind by an
interrupted run is named ``capotest-*``. ``ry`` generates the sync twins.
"""

from __future__ import annotations

import datetime
import json
import time
from collections.abc import AsyncIterator, Iterator

import anyio
import pytest
from capo_eventbridgev2 import AsyncEventBridgeV2Client, Credentials, EventBridgeV2Client
from capo_eventbridgev2.errors import (
    ConflictException,
    InvalidInputException,
    PublicPolicyException,
    ResourceAlreadyExistsException,
    ResourceNotFoundException,
)

from tests.conftest import AWS_REGION, unique_name

DESCRIPTION = "capo integration test, safe to delete"


async def async_wait_until_active(client: AsyncEventBridgeV2Client, arn: str) -> None:
    """Poll a bus out of CREATING; it takes a few seconds, and only then can it be deleted."""
    for _ in range(60):
        if (await client.describe_event_bus(arn)).get("state") == "ACTIVE":
            return
        await anyio.sleep(1)
    raise TimeoutError(f"{arn} did not become ACTIVE")


def wait_until_active(client: EventBridgeV2Client, arn: str) -> None:
    """Sync twin of :func:`async_wait_until_active`."""
    for _ in range(60):
        if client.describe_event_bus(arn).get("state") == "ACTIVE":
            return
        time.sleep(1)
    raise TimeoutError(f"{arn} did not become ACTIVE")


@pytest.fixture(scope="session")
def eventbridge(aws_credentials: Credentials) -> Iterator[EventBridgeV2Client]:
    with EventBridgeV2Client(region=AWS_REGION) as client:
        yield client


@pytest.fixture
async def async_eventbridge(async_aws_credentials: Credentials) -> AsyncIterator[AsyncEventBridgeV2Client]:
    async with AsyncEventBridgeV2Client(region=AWS_REGION) as client:
        yield client


@pytest.fixture
def event_bus(eventbridge: EventBridgeV2Client) -> Iterator[str]:
    """ARN of a fresh ACTIVE event bus, deleted after the test."""
    created = eventbridge.create_event_bus(unique_name(), description=DESCRIPTION, tags={"project": "capo"})
    arn = created.get("event_bus_arn", "")
    wait_until_active(eventbridge, arn)
    try:
        yield arn
    finally:
        eventbridge.delete_event_bus(arn)


class TestAsyncReadOnly:  # unasync: generate
    async def test_list_event_buses(self, async_eventbridge: AsyncEventBridgeV2Client):
        listed = await async_eventbridge.list_event_buses(max_results=1)
        assert len(listed.get("event_buses", [])) <= 1

    async def test_invalid_input_is_a_modeled_error(self, async_eventbridge: AsyncEventBridgeV2Client):
        with pytest.raises(InvalidInputException) as info:
            await async_eventbridge.create_event_bus("not a valid name!")
        assert "not a valid name!" in info.value.data.get("message", "")


class TestReadOnly:  # unasync: generated
    def test_list_event_buses(self, eventbridge: EventBridgeV2Client):
        listed = eventbridge.list_event_buses(max_results=1)
        assert len(listed.get("event_buses", [])) <= 1

    def test_invalid_input_is_a_modeled_error(self, eventbridge: EventBridgeV2Client):
        with pytest.raises(InvalidInputException) as info:
            eventbridge.create_event_bus("not a valid name!")
        assert "not a valid name!" in info.value.data.get("message", "")


class TestAsyncEventBus:  # unasync: generate
    pytestmark = pytest.mark.paid

    async def test_create_describe_update_delete(self, async_eventbridge: AsyncEventBridgeV2Client):
        name = unique_name()
        created = await async_eventbridge.create_event_bus(
            name, description=DESCRIPTION, storage_configuration={"retention_period_in_days": 2}
        )
        arn = created.get("event_bus_arn", "")
        await async_wait_until_active(async_eventbridge, arn)
        try:
            assert created.get("name") == name
            assert created.get("state") == "CREATING"
            assert created.get("storage_configuration", {}).get("retention_period_in_days") == 2
            # timestamps travel as CBOR tag 1 and come back as aware datetimes
            creation_time = created.get("creation_time")
            assert creation_time is not None and creation_time.tzinfo is not None

            described = await async_eventbridge.describe_event_bus(arn)
            assert described.get("description") == DESCRIPTION
            assert described.get("creation_time") == creation_time

            updated = await async_eventbridge.update_event_bus(arn, description="updated")
            assert updated.get("description") == "updated"
            assert (await async_eventbridge.describe_event_bus(arn)).get("description") == "updated"
        finally:
            await async_eventbridge.delete_event_bus(arn)

        with pytest.raises(ResourceNotFoundException):
            for _ in range(60):  # DELETING for a few seconds, then gone
                await async_eventbridge.describe_event_bus(arn)
                await anyio.sleep(1)

    async def test_duplicate_name_raises(self, async_eventbridge: AsyncEventBridgeV2Client, event_bus: str):
        with pytest.raises(ResourceAlreadyExistsException):
            await async_eventbridge.create_event_bus(event_bus.split("/")[1])

    async def test_list_paginates(self, async_eventbridge: AsyncEventBridgeV2Client, event_bus: str):
        name = event_bus.split("/")[1]
        created = await async_eventbridge.create_event_bus(f"{name}-b", description=DESCRIPTION)
        second = created.get("event_bus_arn", "")
        await async_wait_until_active(async_eventbridge, second)
        try:
            page = await async_eventbridge.list_event_buses(name_prefix=name, max_results=1)
            assert len(page.get("event_buses", [])) == 1
            assert page.get("next_token")

            listed = [bus async for bus in async_eventbridge.iter_list_event_buses(name_prefix=name, max_results=1)]
            assert sorted(bus.get("event_bus_arn", "") for bus in listed) == sorted([event_bus, second])
        finally:
            await async_eventbridge.delete_event_bus(second)

    async def test_tags(self, async_eventbridge: AsyncEventBridgeV2Client, event_bus: str):
        assert (await async_eventbridge.list_tags_for_resource(event_bus)).get("tags") == {"project": "capo"}

        await async_eventbridge.tag_resource(event_bus, {"stage": "test"})
        assert (await async_eventbridge.list_tags_for_resource(event_bus)).get("tags") == {
            "project": "capo",
            "stage": "test",
        }

        await async_eventbridge.untag_resource(event_bus, ["project"])
        assert (await async_eventbridge.list_tags_for_resource(event_bus)).get("tags") == {"stage": "test"}

    async def test_put_events_reports_each_entry(self, async_eventbridge: AsyncEventBridgeV2Client, event_bus: str):
        out = await async_eventbridge.put_events(
            event_bus,
            [
                {
                    "source": "capo.test",
                    "detail_type": "integration",
                    "detail": json.dumps({"n": 1}),
                    "time": datetime.datetime(2026, 10, 1, 12, 0, tzinfo=datetime.timezone.utc),
                    "resources": [event_bus],
                },
                {"source": "capo.test", "detail_type": "integration", "detail": "not json"},
            ],
        )
        published, rejected = out.get("entries", [])
        assert out.get("failed_entry_count") == 1
        assert published.get("event_id") and published.get("success_code") == "PUBLISHED"
        assert rejected.get("error_code") and "event_id" not in rejected

    async def test_put_raw_events_sends_binary_data(self, async_eventbridge: AsyncEventBridgeV2Client, event_bus: str):
        out = await async_eventbridge.put_raw_events(
            event_bus,
            [
                {
                    "data": b'{"hello": "capo"}',
                    "system_metadata": {"content_type": "application/json"},
                    "metadata": {"origin": "capo"},
                },
                # not valid UTF-8: only survives as a CBOR byte string
                {"data": bytes(range(256)), "system_metadata": {"content_type": "application/octet-stream"}},
            ],
        )
        assert out.get("failed_entry_count") == 0
        assert [entry.get("success_code") for entry in out.get("entries", [])] == ["PUBLISHED", "PUBLISHED"]

    async def test_put_events_to_missing_bus_raises(self, async_eventbridge: AsyncEventBridgeV2Client, event_bus: str):
        missing = event_bus[:-4] + "0000"  # same name, another bus id
        with pytest.raises(ResourceNotFoundException):
            # entries are validated before the bus is looked up, so this one has to be valid
            await async_eventbridge.put_events(
                missing,
                [{"source": "capo.test", "detail_type": "integration", "detail": "{}"}],
            )

    async def test_resource_policy(self, async_eventbridge: AsyncEventBridgeV2Client, event_bus: str):
        account = event_bus.split(":")[4]
        with pytest.raises(ResourceNotFoundException):
            await async_eventbridge.get_resource_policy(event_bus)

        statement = {"Sid": "capo", "Effect": "Allow", "Action": "events:PutEvents", "Resource": event_bus}
        document = json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [{**statement, "Principal": {"AWS": f"arn:aws:iam::{account}:root"}}],
            }
        )
        put = await async_eventbridge.put_resource_policy(event_bus, document, expected_revision_id="NO_POLICY")
        assert put.get("policy_name") == "default"

        got = await async_eventbridge.get_resource_policy(event_bus)
        assert json.loads(got.get("policy_document", "")) == json.loads(document)
        assert got.get("revision_id") == put.get("revision_id")
        assert (await async_eventbridge.list_resource_policies(event_bus)).get("policy_summaries") == [
            {"policy_name": "default", "revision_id": put.get("revision_id")}
        ]

        # the create-only precondition no longer holds
        with pytest.raises(ConflictException):
            await async_eventbridge.put_resource_policy(event_bus, document, expected_revision_id="NO_POLICY")
        public = json.dumps({"Version": "2012-10-17", "Statement": [{**statement, "Principal": "*"}]})
        with pytest.raises(PublicPolicyException):
            await async_eventbridge.put_resource_policy(event_bus, public)

        await async_eventbridge.delete_resource_policy(event_bus, expected_revision_id=put.get("revision_id"))
        assert (await async_eventbridge.list_resource_policies(event_bus)).get("policy_summaries") == []


class TestEventBus:  # unasync: generated
    pytestmark = pytest.mark.paid

    def test_create_describe_update_delete(self, eventbridge: EventBridgeV2Client):
        name = unique_name()
        created = eventbridge.create_event_bus(
            name, description=DESCRIPTION, storage_configuration={"retention_period_in_days": 2}
        )
        arn = created.get("event_bus_arn", "")
        wait_until_active(eventbridge, arn)
        try:
            assert created.get("name") == name
            assert created.get("state") == "CREATING"
            assert created.get("storage_configuration", {}).get("retention_period_in_days") == 2
            # timestamps travel as CBOR tag 1 and come back as aware datetimes
            creation_time = created.get("creation_time")
            assert creation_time is not None and creation_time.tzinfo is not None

            described = eventbridge.describe_event_bus(arn)
            assert described.get("description") == DESCRIPTION
            assert described.get("creation_time") == creation_time

            updated = eventbridge.update_event_bus(arn, description="updated")
            assert updated.get("description") == "updated"
            assert (eventbridge.describe_event_bus(arn)).get("description") == "updated"
        finally:
            eventbridge.delete_event_bus(arn)

        with pytest.raises(ResourceNotFoundException):
            for _ in range(60):  # DELETING for a few seconds, then gone
                eventbridge.describe_event_bus(arn)
                time.sleep(1)

    def test_duplicate_name_raises(self, eventbridge: EventBridgeV2Client, event_bus: str):
        with pytest.raises(ResourceAlreadyExistsException):
            eventbridge.create_event_bus(event_bus.split("/")[1])

    def test_list_paginates(self, eventbridge: EventBridgeV2Client, event_bus: str):
        name = event_bus.split("/")[1]
        created = eventbridge.create_event_bus(f"{name}-b", description=DESCRIPTION)
        second = created.get("event_bus_arn", "")
        wait_until_active(eventbridge, second)
        try:
            page = eventbridge.list_event_buses(name_prefix=name, max_results=1)
            assert len(page.get("event_buses", [])) == 1
            assert page.get("next_token")

            listed = [bus for bus in eventbridge.iter_list_event_buses(name_prefix=name, max_results=1)]
            assert sorted(bus.get("event_bus_arn", "") for bus in listed) == sorted([event_bus, second])
        finally:
            eventbridge.delete_event_bus(second)

    def test_tags(self, eventbridge: EventBridgeV2Client, event_bus: str):
        assert (eventbridge.list_tags_for_resource(event_bus)).get("tags") == {"project": "capo"}

        eventbridge.tag_resource(event_bus, {"stage": "test"})
        assert (eventbridge.list_tags_for_resource(event_bus)).get("tags") == {
            "project": "capo",
            "stage": "test",
        }

        eventbridge.untag_resource(event_bus, ["project"])
        assert (eventbridge.list_tags_for_resource(event_bus)).get("tags") == {"stage": "test"}

    def test_put_events_reports_each_entry(self, eventbridge: EventBridgeV2Client, event_bus: str):
        out = eventbridge.put_events(
            event_bus,
            [
                {
                    "source": "capo.test",
                    "detail_type": "integration",
                    "detail": json.dumps({"n": 1}),
                    "time": datetime.datetime(2026, 10, 1, 12, 0, tzinfo=datetime.timezone.utc),
                    "resources": [event_bus],
                },
                {"source": "capo.test", "detail_type": "integration", "detail": "not json"},
            ],
        )
        published, rejected = out.get("entries", [])
        assert out.get("failed_entry_count") == 1
        assert published.get("event_id") and published.get("success_code") == "PUBLISHED"
        assert rejected.get("error_code") and "event_id" not in rejected

    def test_put_raw_events_sends_binary_data(self, eventbridge: EventBridgeV2Client, event_bus: str):
        out = eventbridge.put_raw_events(
            event_bus,
            [
                {
                    "data": b'{"hello": "capo"}',
                    "system_metadata": {"content_type": "application/json"},
                    "metadata": {"origin": "capo"},
                },
                # not valid UTF-8: only survives as a CBOR byte string
                {"data": bytes(range(256)), "system_metadata": {"content_type": "application/octet-stream"}},
            ],
        )
        assert out.get("failed_entry_count") == 0
        assert [entry.get("success_code") for entry in out.get("entries", [])] == ["PUBLISHED", "PUBLISHED"]

    def test_put_events_to_missing_bus_raises(self, eventbridge: EventBridgeV2Client, event_bus: str):
        missing = event_bus[:-4] + "0000"  # same name, another bus id
        with pytest.raises(ResourceNotFoundException):
            # entries are validated before the bus is looked up, so this one has to be valid
            eventbridge.put_events(
                missing,
                [{"source": "capo.test", "detail_type": "integration", "detail": "{}"}],
            )

    def test_resource_policy(self, eventbridge: EventBridgeV2Client, event_bus: str):
        account = event_bus.split(":")[4]
        with pytest.raises(ResourceNotFoundException):
            eventbridge.get_resource_policy(event_bus)

        statement = {"Sid": "capo", "Effect": "Allow", "Action": "events:PutEvents", "Resource": event_bus}
        document = json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [{**statement, "Principal": {"AWS": f"arn:aws:iam::{account}:root"}}],
            }
        )
        put = eventbridge.put_resource_policy(event_bus, document, expected_revision_id="NO_POLICY")
        assert put.get("policy_name") == "default"

        got = eventbridge.get_resource_policy(event_bus)
        assert json.loads(got.get("policy_document", "")) == json.loads(document)
        assert got.get("revision_id") == put.get("revision_id")
        assert (eventbridge.list_resource_policies(event_bus)).get("policy_summaries") == [
            {"policy_name": "default", "revision_id": put.get("revision_id")}
        ]

        # the create-only precondition no longer holds
        with pytest.raises(ConflictException):
            eventbridge.put_resource_policy(event_bus, document, expected_revision_id="NO_POLICY")
        public = json.dumps({"Version": "2012-10-17", "Statement": [{**statement, "Principal": "*"}]})
        with pytest.raises(PublicPolicyException):
            eventbridge.put_resource_policy(event_bus, public)

        eventbridge.delete_resource_policy(event_bus, expected_revision_id=put.get("revision_id"))
        assert (eventbridge.list_resource_policies(event_bus)).get("policy_summaries") == []
