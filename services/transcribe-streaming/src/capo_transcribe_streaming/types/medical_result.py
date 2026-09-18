"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.boolean
    import capo_transcribe_streaming.types.double
    import capo_transcribe_streaming.types.medical_alternative_list
    import capo_transcribe_streaming.types.string


class MedicalResult(TypedDict, closed=True):
    result_id: NotRequired["capo_transcribe_streaming.types.string.String"]
    """<p>Provides a unique identifier for the <code>Result</code>.</p>"""
    start_time: "capo_transcribe_streaming.types.double.Double"
    """<p>The start time, in seconds, of the <code>Result</code>.</p>"""
    end_time: "capo_transcribe_streaming.types.double.Double"
    """<p>The end time, in seconds, of the <code>Result</code>.</p>"""
    is_partial: "capo_transcribe_streaming.types.boolean.Boolean"
    """<p>Indicates if the segment is complete.</p> <p>If <code>IsPartial</code> is <code>true</code>, the segment is not complete. If <code>IsPartial</code> is <code>false</code>, the segment is complete.</p>"""
    alternatives: NotRequired[
        "capo_transcribe_streaming.types.medical_alternative_list.MedicalAlternativeList"
    ]
    """<p>A list of possible alternative transcriptions for the input audio. Each alternative may contain one or more of <code>Items</code>, <code>Entities</code>, or <code>Transcript</code>.</p>"""
    channel_id: NotRequired["capo_transcribe_streaming.types.string.String"]
    """<p>Indicates the channel identified for the <code>Result</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalResult) -> dict:
    out: dict = {}
    if "result_id" in value:
        out["ResultId"] = value["result_id"]
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
    out["IsPartial"] = value.get("is_partial", False)
    if "alternatives" in value:
        import capo_transcribe_streaming.types.medical_alternative_list

        out["Alternatives"] = (
            capo_transcribe_streaming.types.medical_alternative_list.serialize_json(
                value["alternatives"]
            )
        )
    if "channel_id" in value:
        out["ChannelId"] = value["channel_id"]
    return out


def deserialize_json(data: dict) -> MedicalResult:
    out: MedicalResult = {}  # type: ignore[typeddict-item]
    if data.get("ResultId") is not None:
        out["result_id"] = data["ResultId"]
    if data.get("StartTime") is not None:
        out["start_time"] = float(data["StartTime"])
    else:
        out["start_time"] = 0
    if data.get("EndTime") is not None:
        out["end_time"] = float(data["EndTime"])
    else:
        out["end_time"] = 0
    if data.get("IsPartial") is not None:
        out["is_partial"] = data["IsPartial"]
    else:
        out["is_partial"] = False
    if data.get("Alternatives") is not None:
        import capo_transcribe_streaming.types.medical_alternative_list

        out["alternatives"] = (
            capo_transcribe_streaming.types.medical_alternative_list.deserialize_json(
                data["Alternatives"]
            )
        )
    if data.get("ChannelId") is not None:
        out["channel_id"] = data["ChannelId"]
    return out
