"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PutEventsSystemMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_deduplication_id
    import capo_eventbridgev2.types.event_group_id


class PutEventsSystemMetadata(TypedDict, closed=True):
    event_group_id: NotRequired["capo_eventbridgev2.types.event_group_id.EventGroupId"]
    """Event group ID for FIFO ordering."""
    deduplication_id: NotRequired[
        "capo_eventbridgev2.types.event_deduplication_id.EventDeduplicationId"
    ]
    """Deduplication ID for FIFO deduplication."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutEventsSystemMetadata) -> dict:
    out: dict = {}
    if "event_group_id" in value:
        out["EventGroupId"] = value["event_group_id"]
    if "deduplication_id" in value:
        out["DeduplicationId"] = value["deduplication_id"]
    return out


def deserialize_cbor(data: dict) -> PutEventsSystemMetadata:
    out: PutEventsSystemMetadata = {}  # type: ignore[typeddict-item]
    if data.get("EventGroupId") is not None:
        out["event_group_id"] = data["EventGroupId"]
    if data.get("DeduplicationId") is not None:
        out["deduplication_id"] = data["DeduplicationId"]
    return out
