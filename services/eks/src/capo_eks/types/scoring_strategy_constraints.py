"""Generated from Smithy shape ``com.amazonaws.eks#ScoringStrategyConstraints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.allowed_values_constraint
    import capo_eks.types.resource_constraints


class ScoringStrategyConstraints(TypedDict, closed=True):
    scoring_strategy: NotRequired[
        "capo_eks.types.allowed_values_constraint.AllowedValuesConstraint"
    ]
    """<p>The allowed values for the scoring strategy type.</p>"""
    resources: NotRequired["capo_eks.types.resource_constraints.ResourceConstraints"]
    """<p>The constraints for resource weights.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScoringStrategyConstraints) -> dict:
    out: dict = {}
    if "scoring_strategy" in value:
        import capo_eks.types.allowed_values_constraint

        out["scoringStrategy"] = (
            capo_eks.types.allowed_values_constraint.serialize_json(
                value["scoring_strategy"]
            )
        )
    if "resources" in value:
        import capo_eks.types.resource_constraints

        out["resources"] = capo_eks.types.resource_constraints.serialize_json(
            value["resources"]
        )
    return out


def deserialize_json(data: dict) -> ScoringStrategyConstraints:
    out: ScoringStrategyConstraints = {}  # type: ignore[typeddict-item]
    if data.get("scoringStrategy") is not None:
        import capo_eks.types.allowed_values_constraint

        out["scoring_strategy"] = (
            capo_eks.types.allowed_values_constraint.deserialize_json(
                data["scoringStrategy"]
            )
        )
    if data.get("resources") is not None:
        import capo_eks.types.resource_constraints

        out["resources"] = capo_eks.types.resource_constraints.deserialize_json(
            data["resources"]
        )
    return out
