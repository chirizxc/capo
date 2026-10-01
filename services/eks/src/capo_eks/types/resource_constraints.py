"""Generated from Smithy shape ``com.amazonaws.eks#ResourceConstraints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.allowed_values_constraint
    import capo_eks.types.integer_range_constraint


class ResourceConstraints(TypedDict, closed=True):
    name: NotRequired[
        "capo_eks.types.allowed_values_constraint.AllowedValuesConstraint"
    ]
    """<p>The allowed values for resource names.</p>"""
    weight: NotRequired[
        "capo_eks.types.integer_range_constraint.IntegerRangeConstraint"
    ]
    """<p>The allowed range for resource weight values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConstraints) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_eks.types.allowed_values_constraint

        out["name"] = capo_eks.types.allowed_values_constraint.serialize_json(
            value["name"]
        )
    if "weight" in value:
        import capo_eks.types.integer_range_constraint

        out["weight"] = capo_eks.types.integer_range_constraint.serialize_json(
            value["weight"]
        )
    return out


def deserialize_json(data: dict) -> ResourceConstraints:
    out: ResourceConstraints = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_eks.types.allowed_values_constraint

        out["name"] = capo_eks.types.allowed_values_constraint.deserialize_json(
            data["name"]
        )
    if data.get("weight") is not None:
        import capo_eks.types.integer_range_constraint

        out["weight"] = capo_eks.types.integer_range_constraint.deserialize_json(
            data["weight"]
        )
    return out
