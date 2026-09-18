"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.confidence
    import capo_transcribe_streaming.types.double
    import capo_transcribe_streaming.types.item_type
    import capo_transcribe_streaming.types.string


class MedicalItem(TypedDict, closed=True):
    start_time: "capo_transcribe_streaming.types.double.Double"
    """<p>The start time, in seconds, of the transcribed item.</p>"""
    end_time: "capo_transcribe_streaming.types.double.Double"
    """<p>The end time, in seconds, of the transcribed item.</p>"""
    type: NotRequired["capo_transcribe_streaming.types.item_type.ItemType"]
    """<p>The type of item identified. Options are: <code>PRONUNCIATION</code> (spoken words) and <code>PUNCTUATION</code>.</p>"""
    content: NotRequired["capo_transcribe_streaming.types.string.String"]
    """<p>The word or punctuation that was transcribed.</p>"""
    confidence: NotRequired["capo_transcribe_streaming.types.confidence.Confidence"]
    """<p>The confidence score associated with a word or phrase in your transcript.</p> <p>Confidence scores are values between 0 and 1. A larger value indicates a higher probability that the identified item correctly matches the item spoken in your media.</p>"""
    speaker: NotRequired["capo_transcribe_streaming.types.string.String"]
    """<p>If speaker partitioning is enabled, <code>Speaker</code> labels the speaker of the specified item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalItem) -> dict:
    out: dict = {}
    out["StartTime"] = (
        "NaN"
        if value.get("start_time", 0) != value.get("start_time", 0)
        else "Infinity"
        if value.get("start_time", 0) == float("inf")
        else "-Infinity"
        if value.get("start_time", 0) == float("-inf")
        else value.get("start_time", 0)
    )
    out["EndTime"] = (
        "NaN"
        if value.get("end_time", 0) != value.get("end_time", 0)
        else "Infinity"
        if value.get("end_time", 0) == float("inf")
        else "-Infinity"
        if value.get("end_time", 0) == float("-inf")
        else value.get("end_time", 0)
    )
    if "type" in value:
        import capo_transcribe_streaming.types.item_type

        out["Type"] = capo_transcribe_streaming.types.item_type.serialize_json(
            value["type"]
        )
    if "content" in value:
        out["Content"] = value["content"]
    if "confidence" in value:
        out["Confidence"] = (
            "NaN"
            if value["confidence"] != value["confidence"]
            else "Infinity"
            if value["confidence"] == float("inf")
            else "-Infinity"
            if value["confidence"] == float("-inf")
            else value["confidence"]
        )
    if "speaker" in value:
        out["Speaker"] = value["speaker"]
    return out


def deserialize_json(data: dict) -> MedicalItem:
    out: MedicalItem = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        out["start_time"] = float(data["StartTime"])
    else:
        out["start_time"] = 0
    if data.get("EndTime") is not None:
        out["end_time"] = float(data["EndTime"])
    else:
        out["end_time"] = 0
    if data.get("Type") is not None:
        import capo_transcribe_streaming.types.item_type

        out["type"] = capo_transcribe_streaming.types.item_type.deserialize_json(
            data["Type"]
        )
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    if data.get("Speaker") is not None:
        out["speaker"] = data["Speaker"]
    return out
