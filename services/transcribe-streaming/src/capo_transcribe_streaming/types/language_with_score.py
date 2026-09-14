"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#LanguageWithScore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.double
    import capo_transcribe_streaming.types.language_code


class LanguageWithScore(TypedDict, closed=True):
    language_code: NotRequired[
        "capo_transcribe_streaming.types.language_code.LanguageCode"
    ]
    """<p>The language code of the identified language.</p>"""
    score: "capo_transcribe_streaming.types.double.Double"
    """<p>The confidence score associated with the identified language code. Confidence scores are values between zero and one; larger values indicate a higher confidence in the identified language.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LanguageWithScore) -> dict:
    out: dict = {}
    if "language_code" in value:
        import capo_transcribe_streaming.types.language_code

        out["LanguageCode"] = (
            capo_transcribe_streaming.types.language_code.serialize_json(
                value["language_code"]
            )
        )
    out["Score"] = (
        "NaN"
        if value.get("score", 0) != value.get("score", 0)
        else "Infinity"
        if value.get("score", 0) == float("inf")
        else "-Infinity"
        if value.get("score", 0) == float("-inf")
        else value.get("score", 0)
    )
    return out


def deserialize_json(data: dict) -> LanguageWithScore:
    out: LanguageWithScore = {}  # type: ignore[typeddict-item]
    if data.get("LanguageCode") is not None:
        import capo_transcribe_streaming.types.language_code

        out["language_code"] = (
            capo_transcribe_streaming.types.language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    else:
        out["score"] = 0
    return out
