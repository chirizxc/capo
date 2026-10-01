"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#CreateEventSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.event_source_arn
    import capo_eventbridgev2.types.event_source_name
    import capo_eventbridgev2.types.event_source_state
    import capo_eventbridgev2.types.timestamp


class CreateEventSourceResponse(TypedDict, closed=True):
    event_source_arn: NotRequired[
        "capo_eventbridgev2.types.event_source_arn.EventSourceArn"
    ]
    name: NotRequired["capo_eventbridgev2.types.event_source_name.EventSourceName"]
    event_bus_arn: NotRequired["capo_eventbridgev2.types.event_bus_arn.EventBusArn"]
    state: NotRequired["capo_eventbridgev2.types.event_source_state.EventSourceState"]
    creation_time: NotRequired["capo_eventbridgev2.types.timestamp.Timestamp"]
    """The time the EventSource was created."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateEventSourceResponse) -> dict:
    out: dict = {}
    if "event_source_arn" in value:
        out["EventSourceArn"] = value["event_source_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "event_bus_arn" in value:
        out["EventBusArn"] = value["event_bus_arn"]
    if "state" in value:
        import capo_eventbridgev2.types.event_source_state

        out["State"] = capo_eventbridgev2.types.event_source_state.serialize_cbor(
            value["state"]
        )
    if "creation_time" in value:
        import capo_eventbridgev2.types.timestamp

        out["CreationTime"] = capo_eventbridgev2.types.timestamp.serialize_cbor(
            value["creation_time"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateEventSourceResponse:
    out: CreateEventSourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("EventSourceArn") is not None:
        out["event_source_arn"] = data["EventSourceArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    if data.get("State") is not None:
        import capo_eventbridgev2.types.event_source_state

        out["state"] = capo_eventbridgev2.types.event_source_state.deserialize_cbor(
            data["State"]
        )
    if data.get("CreationTime") is not None:
        import capo_eventbridgev2.types.timestamp

        out["creation_time"] = capo_eventbridgev2.types.timestamp.deserialize_cbor(
            data["CreationTime"]
        )
    return out
