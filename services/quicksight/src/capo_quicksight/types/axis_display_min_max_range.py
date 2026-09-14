"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisDisplayMinMaxRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.double


class AxisDisplayMinMaxRange(TypedDict, closed=True):
    minimum: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The minimum setup for an axis display range.</p>"""
    maximum: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The maximum setup for an axis display range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AxisDisplayMinMaxRange) -> dict:
    out: dict = {}
    if "minimum" in value:
        out["Minimum"] = (
            "NaN"
            if value["minimum"] != value["minimum"]
            else "Infinity"
            if value["minimum"] == float("inf")
            else "-Infinity"
            if value["minimum"] == float("-inf")
            else value["minimum"]
        )
    if "maximum" in value:
        out["Maximum"] = (
            "NaN"
            if value["maximum"] != value["maximum"]
            else "Infinity"
            if value["maximum"] == float("inf")
            else "-Infinity"
            if value["maximum"] == float("-inf")
            else value["maximum"]
        )
    return out


def deserialize_json(data: dict) -> AxisDisplayMinMaxRange:
    out: AxisDisplayMinMaxRange = {}  # type: ignore[typeddict-item]
    if data.get("Minimum") is not None:
        out["minimum"] = float(data["Minimum"])
    if data.get("Maximum") is not None:
        out["maximum"] = float(data["Maximum"])
    return out
