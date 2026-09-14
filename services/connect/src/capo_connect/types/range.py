"""Generated from Smithy shape ``com.amazonaws.connect#Range``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.nullable_proficiency_level


class Range(TypedDict, closed=True):
    min_proficiency_level: NotRequired[
        "capo_connect.types.nullable_proficiency_level.NullableProficiencyLevel"
    ]
    """<p>The minimum proficiency level of the range.</p>"""
    max_proficiency_level: NotRequired[
        "capo_connect.types.nullable_proficiency_level.NullableProficiencyLevel"
    ]
    """<p>The maximum proficiency level of the range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Range) -> dict:
    out: dict = {}
    if "min_proficiency_level" in value:
        out["MinProficiencyLevel"] = (
            "NaN"
            if value["min_proficiency_level"] != value["min_proficiency_level"]
            else "Infinity"
            if value["min_proficiency_level"] == float("inf")
            else "-Infinity"
            if value["min_proficiency_level"] == float("-inf")
            else value["min_proficiency_level"]
        )
    if "max_proficiency_level" in value:
        out["MaxProficiencyLevel"] = (
            "NaN"
            if value["max_proficiency_level"] != value["max_proficiency_level"]
            else "Infinity"
            if value["max_proficiency_level"] == float("inf")
            else "-Infinity"
            if value["max_proficiency_level"] == float("-inf")
            else value["max_proficiency_level"]
        )
    return out


def deserialize_json(data: dict) -> Range:
    out: Range = {}  # type: ignore[typeddict-item]
    if data.get("MinProficiencyLevel") is not None:
        out["min_proficiency_level"] = float(data["MinProficiencyLevel"])
    if data.get("MaxProficiencyLevel") is not None:
        out["max_proficiency_level"] = float(data["MaxProficiencyLevel"])
    return out
