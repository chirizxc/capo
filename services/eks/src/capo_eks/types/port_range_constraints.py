"""Generated from Smithy shape ``com.amazonaws.eks#PortRangeConstraints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.integer_range_constraint


class PortRangeConstraints(TypedDict, closed=True):
    min_port: NotRequired[
        "capo_eks.types.integer_range_constraint.IntegerRangeConstraint"
    ]
    """<p>The constraints for the minimum port value.</p>"""
    max_port: NotRequired[
        "capo_eks.types.integer_range_constraint.IntegerRangeConstraint"
    ]
    """<p>The constraints for the maximum port value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortRangeConstraints) -> dict:
    out: dict = {}
    if "min_port" in value:
        import capo_eks.types.integer_range_constraint

        out["minPort"] = capo_eks.types.integer_range_constraint.serialize_json(
            value["min_port"]
        )
    if "max_port" in value:
        import capo_eks.types.integer_range_constraint

        out["maxPort"] = capo_eks.types.integer_range_constraint.serialize_json(
            value["max_port"]
        )
    return out


def deserialize_json(data: dict) -> PortRangeConstraints:
    out: PortRangeConstraints = {}  # type: ignore[typeddict-item]
    if data.get("minPort") is not None:
        import capo_eks.types.integer_range_constraint

        out["min_port"] = capo_eks.types.integer_range_constraint.deserialize_json(
            data["minPort"]
        )
    if data.get("maxPort") is not None:
        import capo_eks.types.integer_range_constraint

        out["max_port"] = capo_eks.types.integer_range_constraint.deserialize_json(
            data["maxPort"]
        )
    return out
