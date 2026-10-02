"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#SubscriberSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.account_id
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.ordering_type
    import capo_eventbridgev2.types.subscriber_arn
    import capo_eventbridgev2.types.subscriber_name
    import capo_eventbridgev2.types.subscriber_state
    import capo_eventbridgev2.types.target_resource_arn
    import capo_eventbridgev2.types.timestamp


class SubscriberSummary(TypedDict, closed=True):
    subscriber_arn: NotRequired["capo_eventbridgev2.types.subscriber_arn.SubscriberArn"]
    name: NotRequired["capo_eventbridgev2.types.subscriber_name.SubscriberName"]
    event_bus_arn: NotRequired["capo_eventbridgev2.types.event_bus_arn.EventBusArn"]
    target_arn: NotRequired[
        "capo_eventbridgev2.types.target_resource_arn.TargetResourceArn"
    ]
    type: NotRequired["capo_eventbridgev2.types.ordering_type.OrderingType"]
    revoked: NotRequired["bool"]
    """True when the bus owner has revoked this subscriber. Present only when true, so a bus owner listing subscribers sees at a glance which ones they revoked. See DescribeSubscriberResponse$Revoked."""
    state: NotRequired["capo_eventbridgev2.types.subscriber_state.SubscriberState"]
    creation_time: NotRequired["capo_eventbridgev2.types.timestamp.Timestamp"]
    """The time the subscriber was created."""
    last_modified_time: NotRequired["capo_eventbridgev2.types.timestamp.Timestamp"]
    """The time the subscriber was last modified."""
    subscriber_account_id: NotRequired["capo_eventbridgev2.types.account_id.AccountId"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SubscriberSummary) -> dict:
    out: dict = {}
    if "subscriber_arn" in value:
        out["SubscriberArn"] = value["subscriber_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "event_bus_arn" in value:
        out["EventBusArn"] = value["event_bus_arn"]
    if "target_arn" in value:
        out["TargetArn"] = value["target_arn"]
    if "type" in value:
        import capo_eventbridgev2.types.ordering_type

        out["Type"] = capo_eventbridgev2.types.ordering_type.serialize_cbor(
            value["type"]
        )
    if "revoked" in value:
        out["Revoked"] = value["revoked"]
    if "state" in value:
        import capo_eventbridgev2.types.subscriber_state

        out["State"] = capo_eventbridgev2.types.subscriber_state.serialize_cbor(
            value["state"]
        )
    if "creation_time" in value:
        import capo_eventbridgev2.types.timestamp

        out["CreationTime"] = capo_eventbridgev2.types.timestamp.serialize_cbor(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_eventbridgev2.types.timestamp

        out["LastModifiedTime"] = capo_eventbridgev2.types.timestamp.serialize_cbor(
            value["last_modified_time"]
        )
    if "subscriber_account_id" in value:
        out["SubscriberAccountId"] = value["subscriber_account_id"]
    return out


def deserialize_cbor(data: dict) -> SubscriberSummary:
    out: SubscriberSummary = {}  # type: ignore[typeddict-item]
    if data.get("SubscriberArn") is not None:
        out["subscriber_arn"] = data["SubscriberArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    if data.get("TargetArn") is not None:
        out["target_arn"] = data["TargetArn"]
    if data.get("Type") is not None:
        import capo_eventbridgev2.types.ordering_type

        out["type"] = capo_eventbridgev2.types.ordering_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("Revoked") is not None:
        out["revoked"] = data["Revoked"]
    if data.get("State") is not None:
        import capo_eventbridgev2.types.subscriber_state

        out["state"] = capo_eventbridgev2.types.subscriber_state.deserialize_cbor(
            data["State"]
        )
    if data.get("CreationTime") is not None:
        import capo_eventbridgev2.types.timestamp

        out["creation_time"] = capo_eventbridgev2.types.timestamp.deserialize_cbor(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_eventbridgev2.types.timestamp

        out["last_modified_time"] = capo_eventbridgev2.types.timestamp.deserialize_cbor(
            data["LastModifiedTime"]
        )
    if data.get("SubscriberAccountId") is not None:
        out["subscriber_account_id"] = data["SubscriberAccountId"]
    return out
