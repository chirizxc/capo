"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#IntentConfidence``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.double


class IntentConfidence(TypedDict, closed=True):
    score: "capo_lex_runtime_service.types.double.Double"
    """<p>A score that indicates how confident Amazon Lex is that an intent satisfies the user's intent. Ranges between 0.00 and 1.00. Higher scores indicate higher confidence.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentConfidence) -> dict:
    out: dict = {}
    out["score"] = (
        "NaN"
        if value.get("score", 0) != value.get("score", 0)
        else "Infinity"
        if value.get("score", 0) == float("inf")
        else "-Infinity"
        if value.get("score", 0) == float("-inf")
        else value.get("score", 0)
    )
    return out


def deserialize_json(data: dict) -> IntentConfidence:
    out: IntentConfidence = {}  # type: ignore[typeddict-item]
    if data.get("score") is not None:
        out["score"] = float(data["score"])
    else:
        out["score"] = 0
    return out
