"""Generated from Smithy shape ``com.amazonaws.appflow#Range``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.double


class Range(TypedDict, closed=True):
    maximum: "capo_appflow.types.double.Double"
    """<p>Maximum value supported by the field.</p>"""
    minimum: "capo_appflow.types.double.Double"
    """<p>Minimum value supported by the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Range) -> dict:
    out: dict = {}
    out["maximum"] = (
        "NaN"
        if value.get("maximum", 0) != value.get("maximum", 0)
        else "Infinity"
        if value.get("maximum", 0) == float("inf")
        else "-Infinity"
        if value.get("maximum", 0) == float("-inf")
        else value.get("maximum", 0)
    )
    out["minimum"] = (
        "NaN"
        if value.get("minimum", 0) != value.get("minimum", 0)
        else "Infinity"
        if value.get("minimum", 0) == float("inf")
        else "-Infinity"
        if value.get("minimum", 0) == float("-inf")
        else value.get("minimum", 0)
    )
    return out


def deserialize_json(data: dict) -> Range:
    out: Range = {}  # type: ignore[typeddict-item]
    if data.get("maximum") is not None:
        out["maximum"] = float(data["maximum"])
    else:
        out["maximum"] = 0
    if data.get("minimum") is not None:
        out["minimum"] = float(data["minimum"])
    else:
        out["minimum"] = 0
    return out
