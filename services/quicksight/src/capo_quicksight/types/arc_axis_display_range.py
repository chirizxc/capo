"""Generated from Smithy shape ``com.amazonaws.quicksight#ArcAxisDisplayRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.double


class ArcAxisDisplayRange(TypedDict, closed=True):
    min: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The minimum value of the arc axis range.</p>"""
    max: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The maximum value of the arc axis range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArcAxisDisplayRange) -> dict:
    out: dict = {}
    if "min" in value:
        out["Min"] = (
            "NaN"
            if value["min"] != value["min"]
            else "Infinity"
            if value["min"] == float("inf")
            else "-Infinity"
            if value["min"] == float("-inf")
            else value["min"]
        )
    if "max" in value:
        out["Max"] = (
            "NaN"
            if value["max"] != value["max"]
            else "Infinity"
            if value["max"] == float("inf")
            else "-Infinity"
            if value["max"] == float("-inf")
            else value["max"]
        )
    return out


def deserialize_json(data: dict) -> ArcAxisDisplayRange:
    out: ArcAxisDisplayRange = {}  # type: ignore[typeddict-item]
    if data.get("Min") is not None:
        out["min"] = float(data["Min"])
    if data.get("Max") is not None:
        out["max"] = float(data["Max"])
    return out
