"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#CreateSubscriberResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.ordering_type
    import capo_eventbridgev2.types.point_in_time_configuration
    import capo_eventbridgev2.types.starting_position
    import capo_eventbridgev2.types.subscriber_arn
    import capo_eventbridgev2.types.subscriber_name
    import capo_eventbridgev2.types.subscriber_state
    import capo_eventbridgev2.types.timestamp


class CreateSubscriberResponse(TypedDict, closed=True):
    subscriber_arn: NotRequired["capo_eventbridgev2.types.subscriber_arn.SubscriberArn"]
    name: NotRequired["capo_eventbridgev2.types.subscriber_name.SubscriberName"]
    event_bus_arn: NotRequired["capo_eventbridgev2.types.event_bus_arn.EventBusArn"]
    type: NotRequired["capo_eventbridgev2.types.ordering_type.OrderingType"]
    starting_position: NotRequired[
        "capo_eventbridgev2.types.starting_position.StartingPosition"
    ]
    point_in_time_configuration: NotRequired[
        "capo_eventbridgev2.types.point_in_time_configuration.PointInTimeConfiguration"
    ]
    state: NotRequired["capo_eventbridgev2.types.subscriber_state.SubscriberState"]
    creation_time: NotRequired["capo_eventbridgev2.types.timestamp.Timestamp"]
    """The time the subscriber was created."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateSubscriberResponse) -> dict:
    out: dict = {}
    if "subscriber_arn" in value:
        out["SubscriberArn"] = value["subscriber_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "event_bus_arn" in value:
        out["EventBusArn"] = value["event_bus_arn"]
    if "type" in value:
        import capo_eventbridgev2.types.ordering_type

        out["Type"] = capo_eventbridgev2.types.ordering_type.serialize_cbor(
            value["type"]
        )
    if "starting_position" in value:
        import capo_eventbridgev2.types.starting_position

        out["StartingPosition"] = (
            capo_eventbridgev2.types.starting_position.serialize_cbor(
                value["starting_position"]
            )
        )
    if "point_in_time_configuration" in value:
        import capo_eventbridgev2.types.point_in_time_configuration

        out["PointInTimeConfiguration"] = (
            capo_eventbridgev2.types.point_in_time_configuration.serialize_cbor(
                value["point_in_time_configuration"]
            )
        )
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
    return out


def deserialize_cbor(data: dict) -> CreateSubscriberResponse:
    out: CreateSubscriberResponse = {}  # type: ignore[typeddict-item]
    if data.get("SubscriberArn") is not None:
        out["subscriber_arn"] = data["SubscriberArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    if data.get("Type") is not None:
        import capo_eventbridgev2.types.ordering_type

        out["type"] = capo_eventbridgev2.types.ordering_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("StartingPosition") is not None:
        import capo_eventbridgev2.types.starting_position

        out["starting_position"] = (
            capo_eventbridgev2.types.starting_position.deserialize_cbor(
                data["StartingPosition"]
            )
        )
    if data.get("PointInTimeConfiguration") is not None:
        import capo_eventbridgev2.types.point_in_time_configuration

        out["point_in_time_configuration"] = (
            capo_eventbridgev2.types.point_in_time_configuration.deserialize_cbor(
                data["PointInTimeConfiguration"]
            )
        )
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
    return out
