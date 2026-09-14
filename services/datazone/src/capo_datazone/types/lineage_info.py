"""Generated from Smithy shape ``com.amazonaws.datazone#LineageInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.lineage_event_error_message
    import capo_datazone.types.lineage_event_processing_status


class LineageInfo(TypedDict, closed=True):
    event_id: NotRequired["str"]
    """<p>The data lineage event ID.</p>"""
    event_status: NotRequired[
        "capo_datazone.types.lineage_event_processing_status.LineageEventProcessingStatus"
    ]
    """<p>The data lineage event status.</p>"""
    error_message: NotRequired[
        "capo_datazone.types.lineage_event_error_message.LineageEventErrorMessage"
    ]
    """<p>The data lineage error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineageInfo) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "event_status" in value:
        import capo_datazone.types.lineage_event_processing_status

        out["eventStatus"] = (
            capo_datazone.types.lineage_event_processing_status.serialize_json(
                value["event_status"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> LineageInfo:
    out: LineageInfo = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    if data.get("eventStatus") is not None:
        import capo_datazone.types.lineage_event_processing_status

        out["event_status"] = (
            capo_datazone.types.lineage_event_processing_status.deserialize_json(
                data["eventStatus"]
            )
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
