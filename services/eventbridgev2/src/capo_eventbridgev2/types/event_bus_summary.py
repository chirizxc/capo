"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#EventBusSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.account_id
    import capo_eventbridgev2.types.bus_state
    import capo_eventbridgev2.types.description
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.event_bus_name
    import capo_eventbridgev2.types.state_reason
    import capo_eventbridgev2.types.timestamp


class EventBusSummary(TypedDict, closed=True):
    name: NotRequired["capo_eventbridgev2.types.event_bus_name.EventBusName"]
    event_bus_arn: NotRequired["capo_eventbridgev2.types.event_bus_arn.EventBusArn"]
    description: NotRequired["capo_eventbridgev2.types.description.Description"]
    creation_time: NotRequired["capo_eventbridgev2.types.timestamp.Timestamp"]
    """The time the event bus was created."""
    last_modified_time: NotRequired["capo_eventbridgev2.types.timestamp.Timestamp"]
    """The time the event bus was last modified."""
    state: NotRequired["capo_eventbridgev2.types.bus_state.BusState"]
    state_reason: NotRequired["capo_eventbridgev2.types.state_reason.StateReason"]
    event_bus_account_id: NotRequired["capo_eventbridgev2.types.account_id.AccountId"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventBusSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "event_bus_arn" in value:
        out["EventBusArn"] = value["event_bus_arn"]
    if "description" in value:
        out["Description"] = value["description"]
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
    if "state" in value:
        import capo_eventbridgev2.types.bus_state

        out["State"] = capo_eventbridgev2.types.bus_state.serialize_cbor(value["state"])
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "event_bus_account_id" in value:
        out["EventBusAccountId"] = value["event_bus_account_id"]
    return out


def deserialize_cbor(data: dict) -> EventBusSummary:
    out: EventBusSummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
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
    if data.get("State") is not None:
        import capo_eventbridgev2.types.bus_state

        out["state"] = capo_eventbridgev2.types.bus_state.deserialize_cbor(
            data["State"]
        )
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("EventBusAccountId") is not None:
        out["event_bus_account_id"] = data["EventBusAccountId"]
    return out
