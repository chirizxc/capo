"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#EventBusV2Parameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.deduplication_configuration
    import capo_eventbridgev2.types.event_bus_v2_metadata_map
    import capo_eventbridgev2.types.event_bus_v2_system_metadata


class EventBusV2Parameters(TypedDict, closed=True):
    metadata: NotRequired[
        "capo_eventbridgev2.types.event_bus_v2_metadata_map.EventBusV2MetadataMap"
    ]
    """Customer-defined metadata forwarded with each event."""
    system_metadata: NotRequired[
        "capo_eventbridgev2.types.event_bus_v2_system_metadata.EventBusV2SystemMetadata"
    ]
    """Customer-controllable system metadata attached to each forwarded event."""
    deduplication_configuration: NotRequired[
        "capo_eventbridgev2.types.deduplication_configuration.DeduplicationConfiguration"
    ]
    """Deduplication settings applied to the forwarded events on the downstream bus."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventBusV2Parameters) -> dict:
    out: dict = {}
    if "metadata" in value:
        import capo_eventbridgev2.types.event_bus_v2_metadata_map

        out["Metadata"] = (
            capo_eventbridgev2.types.event_bus_v2_metadata_map.serialize_cbor(
                value["metadata"]
            )
        )
    if "system_metadata" in value:
        import capo_eventbridgev2.types.event_bus_v2_system_metadata

        out["SystemMetadata"] = (
            capo_eventbridgev2.types.event_bus_v2_system_metadata.serialize_cbor(
                value["system_metadata"]
            )
        )
    if "deduplication_configuration" in value:
        import capo_eventbridgev2.types.deduplication_configuration

        out["DeduplicationConfiguration"] = (
            capo_eventbridgev2.types.deduplication_configuration.serialize_cbor(
                value["deduplication_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> EventBusV2Parameters:
    out: EventBusV2Parameters = {}  # type: ignore[typeddict-item]
    if data.get("Metadata") is not None:
        import capo_eventbridgev2.types.event_bus_v2_metadata_map

        out["metadata"] = (
            capo_eventbridgev2.types.event_bus_v2_metadata_map.deserialize_cbor(
                data["Metadata"]
            )
        )
    if data.get("SystemMetadata") is not None:
        import capo_eventbridgev2.types.event_bus_v2_system_metadata

        out["system_metadata"] = (
            capo_eventbridgev2.types.event_bus_v2_system_metadata.deserialize_cbor(
                data["SystemMetadata"]
            )
        )
    if data.get("DeduplicationConfiguration") is not None:
        import capo_eventbridgev2.types.deduplication_configuration

        out["deduplication_configuration"] = (
            capo_eventbridgev2.types.deduplication_configuration.deserialize_cbor(
                data["DeduplicationConfiguration"]
            )
        )
    return out
