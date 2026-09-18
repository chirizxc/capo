"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#SentimentScore``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.double


class SentimentScore(TypedDict, closed=True):
    positive: "capo_lex_runtime_v2.types.double.Double"
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its detection of the <code>POSITIVE</code> sentiment.</p>"""
    negative: "capo_lex_runtime_v2.types.double.Double"
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its detection of the <code>NEGATIVE</code> sentiment.</p>"""
    neutral: "capo_lex_runtime_v2.types.double.Double"
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its detection of the <code>NEUTRAL</code> sentiment.</p>"""
    mixed: "capo_lex_runtime_v2.types.double.Double"
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of its detection of the <code>MIXED</code> sentiment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SentimentScore) -> dict:
    out: dict = {}
    out["positive"] = (
        "NaN"
        if value.get("positive", 0) != value.get("positive", 0)
        else "Infinity"
        if value.get("positive", 0) == float("inf")
        else "-Infinity"
        if value.get("positive", 0) == float("-inf")
        else value.get("positive", 0)
    )
    out["negative"] = (
        "NaN"
        if value.get("negative", 0) != value.get("negative", 0)
        else "Infinity"
        if value.get("negative", 0) == float("inf")
        else "-Infinity"
        if value.get("negative", 0) == float("-inf")
        else value.get("negative", 0)
    )
    out["neutral"] = (
        "NaN"
        if value.get("neutral", 0) != value.get("neutral", 0)
        else "Infinity"
        if value.get("neutral", 0) == float("inf")
        else "-Infinity"
        if value.get("neutral", 0) == float("-inf")
        else value.get("neutral", 0)
    )
    out["mixed"] = (
        "NaN"
        if value.get("mixed", 0) != value.get("mixed", 0)
        else "Infinity"
        if value.get("mixed", 0) == float("inf")
        else "-Infinity"
        if value.get("mixed", 0) == float("-inf")
        else value.get("mixed", 0)
    )
    return out


def deserialize_json(data: dict) -> SentimentScore:
    out: SentimentScore = {}  # type: ignore[typeddict-item]
    if data.get("positive") is not None:
        out["positive"] = float(data["positive"])
    else:
        out["positive"] = 0
    if data.get("negative") is not None:
        out["negative"] = float(data["negative"])
    else:
        out["negative"] = 0
    if data.get("neutral") is not None:
        out["neutral"] = float(data["neutral"])
    else:
        out["neutral"] = 0
    if data.get("mixed") is not None:
        out["mixed"] = float(data["mixed"])
    else:
        out["mixed"] = 0
    return out
