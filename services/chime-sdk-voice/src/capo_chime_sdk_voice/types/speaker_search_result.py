"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SpeakerSearchResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.confidence_score
    import capo_chime_sdk_voice.types.non_empty_string256


class SpeakerSearchResult(TypedDict, closed=True):
    confidence_score: "capo_chime_sdk_voice.types.confidence_score.ConfidenceScore"
    """<p>The confidence score in the speaker search analysis.</p>"""
    voice_profile_id: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    ]
    """<p>The voice profile ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpeakerSearchResult) -> dict:
    out: dict = {}
    out["ConfidenceScore"] = (
        "NaN"
        if value.get("confidence_score", 0) != value.get("confidence_score", 0)
        else "Infinity"
        if value.get("confidence_score", 0) == float("inf")
        else "-Infinity"
        if value.get("confidence_score", 0) == float("-inf")
        else value.get("confidence_score", 0)
    )
    if "voice_profile_id" in value:
        out["VoiceProfileId"] = value["voice_profile_id"]
    return out


def deserialize_json(data: dict) -> SpeakerSearchResult:
    out: SpeakerSearchResult = {}  # type: ignore[typeddict-item]
    if data.get("ConfidenceScore") is not None:
        out["confidence_score"] = float(data["ConfidenceScore"])
    else:
        out["confidence_score"] = 0
    if data.get("VoiceProfileId") is not None:
        out["voice_profile_id"] = data["VoiceProfileId"]
    return out
