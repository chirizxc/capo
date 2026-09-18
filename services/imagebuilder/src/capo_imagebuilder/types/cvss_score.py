"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CvssScore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.non_negative_double


class CvssScore(TypedDict, closed=True):
    base_score: NotRequired[
        "capo_imagebuilder.types.non_negative_double.NonNegativeDouble"
    ]
    """<p>The CVSS base score.</p>"""
    scoring_vector: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The vector string of the CVSS score.</p>"""
    version: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The CVSS version that generated the score.</p>"""
    source: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The source of the CVSS score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CvssScore) -> dict:
    out: dict = {}
    if "base_score" in value:
        out["baseScore"] = (
            "NaN"
            if value["base_score"] != value["base_score"]
            else "Infinity"
            if value["base_score"] == float("inf")
            else "-Infinity"
            if value["base_score"] == float("-inf")
            else value["base_score"]
        )
    if "scoring_vector" in value:
        out["scoringVector"] = value["scoring_vector"]
    if "version" in value:
        out["version"] = value["version"]
    if "source" in value:
        out["source"] = value["source"]
    return out


def deserialize_json(data: dict) -> CvssScore:
    out: CvssScore = {}  # type: ignore[typeddict-item]
    if data.get("baseScore") is not None:
        out["base_score"] = float(data["baseScore"])
    if data.get("scoringVector") is not None:
        out["scoring_vector"] = data["scoringVector"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("source") is not None:
        out["source"] = data["source"]
    return out
