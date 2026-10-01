"""Generated from Smithy shape ``com.amazonaws.eks#IntegerConstraints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.boxed_integer


class IntegerConstraints(TypedDict, closed=True):
    min: NotRequired["capo_eks.types.boxed_integer.BoxedInteger"]
    """<p>The minimum allowed value.</p>"""
    max: NotRequired["capo_eks.types.boxed_integer.BoxedInteger"]
    """<p>The maximum allowed value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegerConstraints) -> dict:
    out: dict = {}
    if "min" in value:
        out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_json(data: dict) -> IntegerConstraints:
    out: IntegerConstraints = {}  # type: ignore[typeddict-item]
    if data.get("min") is not None:
        out["min"] = data["min"]
    if data.get("max") is not None:
        out["max"] = data["max"]
    return out
