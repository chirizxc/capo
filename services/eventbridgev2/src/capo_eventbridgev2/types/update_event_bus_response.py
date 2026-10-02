"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#UpdateEventBusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.bus_state
    import capo_eventbridgev2.types.description
    import capo_eventbridgev2.types.encryption_configuration
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.event_bus_name
    import capo_eventbridgev2.types.state_reason
    import capo_eventbridgev2.types.storage_configuration_output
    import capo_eventbridgev2.types.timestamp


class UpdateEventBusResponse(TypedDict, closed=True):
    event_bus_arn: NotRequired["capo_eventbridgev2.types.event_bus_arn.EventBusArn"]
    name: NotRequired["capo_eventbridgev2.types.event_bus_name.EventBusName"]
    description: NotRequired["capo_eventbridgev2.types.description.Description"]
    encryption_configuration: NotRequired[
        "capo_eventbridgev2.types.encryption_configuration.EncryptionConfiguration"
    ]
    storage_configuration: NotRequired[
        "capo_eventbridgev2.types.storage_configuration_output.StorageConfigurationOutput"
    ]
    state: NotRequired["capo_eventbridgev2.types.bus_state.BusState"]
    state_reason: NotRequired["capo_eventbridgev2.types.state_reason.StateReason"]
    last_modified_time: NotRequired["capo_eventbridgev2.types.timestamp.Timestamp"]
    """The time the event bus was last modified."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateEventBusResponse) -> dict:
    out: dict = {}
    if "event_bus_arn" in value:
        out["EventBusArn"] = value["event_bus_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "encryption_configuration" in value:
        import capo_eventbridgev2.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_eventbridgev2.types.encryption_configuration.serialize_cbor(
                value["encryption_configuration"]
            )
        )
    if "storage_configuration" in value:
        import capo_eventbridgev2.types.storage_configuration_output

        out["StorageConfiguration"] = (
            capo_eventbridgev2.types.storage_configuration_output.serialize_cbor(
                value["storage_configuration"]
            )
        )
    if "state" in value:
        import capo_eventbridgev2.types.bus_state

        out["State"] = capo_eventbridgev2.types.bus_state.serialize_cbor(value["state"])
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "last_modified_time" in value:
        import capo_eventbridgev2.types.timestamp

        out["LastModifiedTime"] = capo_eventbridgev2.types.timestamp.serialize_cbor(
            value["last_modified_time"]
        )
    return out


def deserialize_cbor(data: dict) -> UpdateEventBusResponse:
    out: UpdateEventBusResponse = {}  # type: ignore[typeddict-item]
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EncryptionConfiguration") is not None:
        import capo_eventbridgev2.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_eventbridgev2.types.encryption_configuration.deserialize_cbor(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("StorageConfiguration") is not None:
        import capo_eventbridgev2.types.storage_configuration_output

        out["storage_configuration"] = (
            capo_eventbridgev2.types.storage_configuration_output.deserialize_cbor(
                data["StorageConfiguration"]
            )
        )
    if data.get("State") is not None:
        import capo_eventbridgev2.types.bus_state

        out["state"] = capo_eventbridgev2.types.bus_state.deserialize_cbor(
            data["State"]
        )
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("LastModifiedTime") is not None:
        import capo_eventbridgev2.types.timestamp

        out["last_modified_time"] = capo_eventbridgev2.types.timestamp.deserialize_cbor(
            data["LastModifiedTime"]
        )
    return out
