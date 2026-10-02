"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PutEventsResultEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.error_code
    import capo_eventbridgev2.types.error_message
    import capo_eventbridgev2.types.event_id
    import capo_eventbridgev2.types.sequence_number
    import capo_eventbridgev2.types.success_code


class PutEventsResultEntry(TypedDict, closed=True):
    event_id: NotRequired["capo_eventbridgev2.types.event_id.EventId"]
    sequence_number: NotRequired[
        "capo_eventbridgev2.types.sequence_number.SequenceNumber"
    ]
    success_code: NotRequired["capo_eventbridgev2.types.success_code.SuccessCode"]
    error_code: NotRequired["capo_eventbridgev2.types.error_code.ErrorCode"]
    error_message: NotRequired["capo_eventbridgev2.types.error_message.ErrorMessage"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutEventsResultEntry) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["EventId"] = value["event_id"]
    if "sequence_number" in value:
        out["SequenceNumber"] = value["sequence_number"]
    if "success_code" in value:
        import capo_eventbridgev2.types.success_code

        out["SuccessCode"] = capo_eventbridgev2.types.success_code.serialize_cbor(
            value["success_code"]
        )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> PutEventsResultEntry:
    out: PutEventsResultEntry = {}  # type: ignore[typeddict-item]
    if data.get("EventId") is not None:
        out["event_id"] = data["EventId"]
    if data.get("SequenceNumber") is not None:
        out["sequence_number"] = data["SequenceNumber"]
    if data.get("SuccessCode") is not None:
        import capo_eventbridgev2.types.success_code

        out["success_code"] = capo_eventbridgev2.types.success_code.deserialize_cbor(
            data["SuccessCode"]
        )
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
