"""Generated from Smithy shape ``com.amazonaws.inspector2#NumberFilter``."""

from typing_extensions import NotRequired, TypedDict


class NumberFilter(TypedDict, closed=True):
    upper_inclusive: NotRequired["float"]
    """<p>The highest number to be included in the filter.</p>"""
    lower_inclusive: NotRequired["float"]
    """<p>The lowest number to be included in the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumberFilter) -> dict:
    out: dict = {}
    if "upper_inclusive" in value:
        out["upperInclusive"] = (
            "NaN"
            if value["upper_inclusive"] != value["upper_inclusive"]
            else "Infinity"
            if value["upper_inclusive"] == float("inf")
            else "-Infinity"
            if value["upper_inclusive"] == float("-inf")
            else value["upper_inclusive"]
        )
    if "lower_inclusive" in value:
        out["lowerInclusive"] = (
            "NaN"
            if value["lower_inclusive"] != value["lower_inclusive"]
            else "Infinity"
            if value["lower_inclusive"] == float("inf")
            else "-Infinity"
            if value["lower_inclusive"] == float("-inf")
            else value["lower_inclusive"]
        )
    return out


def deserialize_json(data: dict) -> NumberFilter:
    out: NumberFilter = {}  # type: ignore[typeddict-item]
    if data.get("upperInclusive") is not None:
        out["upper_inclusive"] = float(data["upperInclusive"])
    if data.get("lowerInclusive") is not None:
        out["lower_inclusive"] = float(data["lowerInclusive"])
    return out
