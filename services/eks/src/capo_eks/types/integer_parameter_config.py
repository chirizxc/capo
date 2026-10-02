"""Generated from Smithy shape ``com.amazonaws.eks#IntegerParameterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.boxed_integer
    import capo_eks.types.integer_constraints


class IntegerParameterConfig(TypedDict, closed=True):
    default_value: NotRequired["capo_eks.types.boxed_integer.BoxedInteger"]
    """<p>The default value for the integer parameter.</p>"""
    constraints: NotRequired["capo_eks.types.integer_constraints.IntegerConstraints"]
    """<p>The constraints for the integer parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegerParameterConfig) -> dict:
    out: dict = {}
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "constraints" in value:
        import capo_eks.types.integer_constraints

        out["constraints"] = capo_eks.types.integer_constraints.serialize_json(
            value["constraints"]
        )
    return out


def deserialize_json(data: dict) -> IntegerParameterConfig:
    out: IntegerParameterConfig = {}  # type: ignore[typeddict-item]
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    if data.get("constraints") is not None:
        import capo_eks.types.integer_constraints

        out["constraints"] = capo_eks.types.integer_constraints.deserialize_json(
            data["constraints"]
        )
    return out
