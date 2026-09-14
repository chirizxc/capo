"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisLogarithmicScale``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.double


class AxisLogarithmicScale(TypedDict, closed=True):
    base: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The base setup of a logarithmic axis scale.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AxisLogarithmicScale) -> dict:
    out: dict = {}
    if "base" in value:
        out["Base"] = (
            "NaN"
            if value["base"] != value["base"]
            else "Infinity"
            if value["base"] == float("inf")
            else "-Infinity"
            if value["base"] == float("-inf")
            else value["base"]
        )
    return out


def deserialize_json(data: dict) -> AxisLogarithmicScale:
    out: AxisLogarithmicScale = {}  # type: ignore[typeddict-item]
    if data.get("Base") is not None:
        out["base"] = float(data["Base"])
    return out
