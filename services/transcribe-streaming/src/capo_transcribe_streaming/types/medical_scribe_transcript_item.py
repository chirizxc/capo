"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeTranscriptItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.confidence
    import capo_transcribe_streaming.types.double
    import capo_transcribe_streaming.types.medical_scribe_transcript_item_type
    import capo_transcribe_streaming.types.nullable_boolean
    import capo_transcribe_streaming.types.string


class MedicalScribeTranscriptItem(TypedDict, closed=True):
    begin_audio_time: "capo_transcribe_streaming.types.double.Double"
    """<p>The start time, in milliseconds, of the transcribed item.</p>"""
    end_audio_time: "capo_transcribe_streaming.types.double.Double"
    """<p>The end time, in milliseconds, of the transcribed item.</p>"""
    type: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_transcript_item_type.MedicalScribeTranscriptItemType"
    ]
    """<p>The type of item identified. Options are: <code>PRONUNCIATION</code> (spoken words) and <code>PUNCTUATION</code>. </p>"""
    confidence: NotRequired["capo_transcribe_streaming.types.confidence.Confidence"]
    """<p>The confidence score associated with a word or phrase in your transcript.</p> <p>Confidence scores are values between 0 and 1. A larger value indicates a higher probability that the identified item correctly matches the item spoken in your media. </p>"""
    content: NotRequired["capo_transcribe_streaming.types.string.String"]
    """<p>The word, phrase or punctuation mark that was transcribed.</p>"""
    vocabulary_filter_match: NotRequired[
        "capo_transcribe_streaming.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Indicates whether the specified item matches a word in the vocabulary filter included in your configuration event. If <code>true</code>, there is a vocabulary filter match. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeTranscriptItem) -> dict:
    out: dict = {}
    out["BeginAudioTime"] = (
        "NaN"
        if value.get("begin_audio_time", 0) != value.get("begin_audio_time", 0)
        else "Infinity"
        if value.get("begin_audio_time", 0) == float("inf")
        else "-Infinity"
        if value.get("begin_audio_time", 0) == float("-inf")
        else value.get("begin_audio_time", 0)
    )
    out["EndAudioTime"] = (
        "NaN"
        if value.get("end_audio_time", 0) != value.get("end_audio_time", 0)
        else "Infinity"
        if value.get("end_audio_time", 0) == float("inf")
        else "-Infinity"
        if value.get("end_audio_time", 0) == float("-inf")
        else value.get("end_audio_time", 0)
    )
    if "type" in value:
        import capo_transcribe_streaming.types.medical_scribe_transcript_item_type

        out["Type"] = (
            capo_transcribe_streaming.types.medical_scribe_transcript_item_type.serialize_json(
                value["type"]
            )
        )
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
    if "content" in value:
        out["Content"] = value["content"]
    if "vocabulary_filter_match" in value:
        out["VocabularyFilterMatch"] = value["vocabulary_filter_match"]
    return out


def deserialize_json(data: dict) -> MedicalScribeTranscriptItem:
    out: MedicalScribeTranscriptItem = {}  # type: ignore[typeddict-item]
    if data.get("BeginAudioTime") is not None:
        out["begin_audio_time"] = float(data["BeginAudioTime"])
    else:
        out["begin_audio_time"] = 0
    if data.get("EndAudioTime") is not None:
        out["end_audio_time"] = float(data["EndAudioTime"])
    else:
        out["end_audio_time"] = 0
    if data.get("Type") is not None:
        import capo_transcribe_streaming.types.medical_scribe_transcript_item_type

        out["type"] = (
            capo_transcribe_streaming.types.medical_scribe_transcript_item_type.deserialize_json(
                data["Type"]
            )
        )
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("VocabularyFilterMatch") is not None:
        out["vocabulary_filter_match"] = data["VocabularyFilterMatch"]
    return out
