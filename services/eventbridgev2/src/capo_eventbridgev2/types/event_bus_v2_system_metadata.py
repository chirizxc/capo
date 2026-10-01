"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#EventBusV2SystemMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.string


class EventBusV2SystemMetadata(TypedDict, closed=True):
    event_group_id: NotRequired["capo_eventbridgev2.types.string.String"]
    """Event group ID for FIFO ordering on the downstream bus. Accepts a literal or a JSONata expression."""
    deduplication_id: NotRequired["capo_eventbridgev2.types.string.String"]
    """Deduplication ID for FIFO deduplication on the downstream bus. Accepts a literal or a JSONata expression."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventBusV2SystemMetadata) -> dict:
    out: dict = {}
    if "event_group_id" in value:
        out["EventGroupId"] = value["event_group_id"]
    if "deduplication_id" in value:
        out["DeduplicationId"] = value["deduplication_id"]
    return out


def deserialize_cbor(data: dict) -> EventBusV2SystemMetadata:
    out: EventBusV2SystemMetadata = {}  # type: ignore[typeddict-item]
    if data.get("EventGroupId") is not None:
        out["event_group_id"] = data["EventGroupId"]
    if data.get("DeduplicationId") is not None:
        out["deduplication_id"] = data["DeduplicationId"]
    return out
