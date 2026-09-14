"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeTranscriptSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.audio_offset
    import capo_connecthealth.types.non_null_boolean


class MedicalScribeTranscriptSegment(TypedDict, closed=True):
    segment_id: NotRequired["str"]
    """<p>The unique identifier for this segment</p>"""
    audio_begin_offset: NotRequired["capo_connecthealth.types.audio_offset.AudioOffset"]
    """<p>The offset from audio start when the audio for this segment begins</p>"""
    audio_end_offset: NotRequired["capo_connecthealth.types.audio_offset.AudioOffset"]
    """<p>The offset from audio start when the audio for this segment ends</p>"""
    is_partial: NotRequired["capo_connecthealth.types.non_null_boolean.NonNullBoolean"]
    """<p>Indicates whether this is a partial or final transcript</p>"""
    channel_id: NotRequired["str"]
    """<p>The channel identifier for this segment</p>"""
    content: NotRequired["str"]
    """<p>The transcript text content</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeTranscriptSegment) -> dict:
    out: dict = {}
    if "segment_id" in value:
        out["segmentId"] = value["segment_id"]
    if "audio_begin_offset" in value:
        out["audioBeginOffset"] = (
            "NaN"
            if value["audio_begin_offset"] != value["audio_begin_offset"]
            else "Infinity"
            if value["audio_begin_offset"] == float("inf")
            else "-Infinity"
            if value["audio_begin_offset"] == float("-inf")
            else value["audio_begin_offset"]
        )
    if "audio_end_offset" in value:
        out["audioEndOffset"] = (
            "NaN"
            if value["audio_end_offset"] != value["audio_end_offset"]
            else "Infinity"
            if value["audio_end_offset"] == float("inf")
            else "-Infinity"
            if value["audio_end_offset"] == float("-inf")
            else value["audio_end_offset"]
        )
    if "is_partial" in value:
        out["isPartial"] = value["is_partial"]
    if "channel_id" in value:
        out["channelId"] = value["channel_id"]
    if "content" in value:
        out["content"] = value["content"]
    return out


def deserialize_json(data: dict) -> MedicalScribeTranscriptSegment:
    out: MedicalScribeTranscriptSegment = {}  # type: ignore[typeddict-item]
    if data.get("segmentId") is not None:
        out["segment_id"] = data["segmentId"]
    if data.get("audioBeginOffset") is not None:
        out["audio_begin_offset"] = float(data["audioBeginOffset"])
    if data.get("audioEndOffset") is not None:
        out["audio_end_offset"] = float(data["audioEndOffset"])
    if data.get("isPartial") is not None:
        out["is_partial"] = data["isPartial"]
    if data.get("channelId") is not None:
        out["channel_id"] = data["channelId"]
    if data.get("content") is not None:
        out["content"] = data["content"]
    return out
