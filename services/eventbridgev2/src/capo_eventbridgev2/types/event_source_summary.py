"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#EventSourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.account_id
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.event_source_arn
    import capo_eventbridgev2.types.event_source_name
    import capo_eventbridgev2.types.event_source_state
    import capo_eventbridgev2.types.event_source_type
    import capo_eventbridgev2.types.timestamp


class EventSourceSummary(TypedDict, closed=True):
    event_source_arn: NotRequired[
        "capo_eventbridgev2.types.event_source_arn.EventSourceArn"
    ]
    name: NotRequired["capo_eventbridgev2.types.event_source_name.EventSourceName"]
    event_bus_arn: NotRequired["capo_eventbridgev2.types.event_bus_arn.EventBusArn"]
    type: NotRequired["capo_eventbridgev2.types.event_source_type.EventSourceType"]
    state: NotRequired["capo_eventbridgev2.types.event_source_state.EventSourceState"]
    revoked: NotRequired["bool"]
    """True when the bus owner has withdrawn this EventSource. Present only when true, so a bus owner listing EventSources sees at a glance which ones they revoked. See DescribeEventSourceResponse$Revoked."""
    creation_time: NotRequired["capo_eventbridgev2.types.timestamp.Timestamp"]
    """The time the EventSource was created."""
    last_modified_time: NotRequired["capo_eventbridgev2.types.timestamp.Timestamp"]
    """The time the EventSource was last modified."""
    event_source_account_id: NotRequired[
        "capo_eventbridgev2.types.account_id.AccountId"
    ]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventSourceSummary) -> dict:
    out: dict = {}
    if "event_source_arn" in value:
        out["EventSourceArn"] = value["event_source_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "event_bus_arn" in value:
        out["EventBusArn"] = value["event_bus_arn"]
    if "type" in value:
        import capo_eventbridgev2.types.event_source_type

        out["Type"] = capo_eventbridgev2.types.event_source_type.serialize_cbor(
            value["type"]
        )
    if "state" in value:
        import capo_eventbridgev2.types.event_source_state

        out["State"] = capo_eventbridgev2.types.event_source_state.serialize_cbor(
            value["state"]
        )
    if "revoked" in value:
        out["Revoked"] = value["revoked"]
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
    if "event_source_account_id" in value:
        out["EventSourceAccountId"] = value["event_source_account_id"]
    return out


def deserialize_cbor(data: dict) -> EventSourceSummary:
    out: EventSourceSummary = {}  # type: ignore[typeddict-item]
    if data.get("EventSourceArn") is not None:
        out["event_source_arn"] = data["EventSourceArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    if data.get("Type") is not None:
        import capo_eventbridgev2.types.event_source_type

        out["type"] = capo_eventbridgev2.types.event_source_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("State") is not None:
        import capo_eventbridgev2.types.event_source_state

        out["state"] = capo_eventbridgev2.types.event_source_state.deserialize_cbor(
            data["State"]
        )
    if data.get("Revoked") is not None:
        out["revoked"] = data["Revoked"]
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
    if data.get("EventSourceAccountId") is not None:
        out["event_source_account_id"] = data["EventSourceAccountId"]
    return out
