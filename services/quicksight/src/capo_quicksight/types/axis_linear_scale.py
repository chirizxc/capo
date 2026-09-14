"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisLinearScale``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.double
    import capo_quicksight.types.integer


class AxisLinearScale(TypedDict, closed=True):
    step_count: NotRequired["capo_quicksight.types.integer.Integer"]
    """<p>The step count setup of a linear axis.</p>"""
    step_size: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The step size setup of a linear axis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AxisLinearScale) -> dict:
    out: dict = {}
    if "step_count" in value:
        out["StepCount"] = value["step_count"]
    if "step_size" in value:
        out["StepSize"] = (
            "NaN"
            if value["step_size"] != value["step_size"]
            else "Infinity"
            if value["step_size"] == float("inf")
            else "-Infinity"
            if value["step_size"] == float("-inf")
            else value["step_size"]
        )
    return out


def deserialize_json(data: dict) -> AxisLinearScale:
    out: AxisLinearScale = {}  # type: ignore[typeddict-item]
    if data.get("StepCount") is not None:
        out["step_count"] = data["StepCount"]
    if data.get("StepSize") is not None:
        out["step_size"] = float(data["StepSize"])
    return out
