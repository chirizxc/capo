"""Generated from Smithy shape ``com.amazonaws.eks#ScoringStrategyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.scoring_strategy
    import capo_eks.types.scoring_strategy_constraints


class ScoringStrategyConfig(TypedDict, closed=True):
    default_value: NotRequired["capo_eks.types.scoring_strategy.ScoringStrategy"]
    """<p>The default scoring strategy.</p>"""
    constraints: NotRequired[
        "capo_eks.types.scoring_strategy_constraints.ScoringStrategyConstraints"
    ]
    """<p>The constraints for the scoring strategy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScoringStrategyConfig) -> dict:
    out: dict = {}
    if "default_value" in value:
        import capo_eks.types.scoring_strategy

        out["defaultValue"] = capo_eks.types.scoring_strategy.serialize_json(
            value["default_value"]
        )
    if "constraints" in value:
        import capo_eks.types.scoring_strategy_constraints

        out["constraints"] = capo_eks.types.scoring_strategy_constraints.serialize_json(
            value["constraints"]
        )
    return out


def deserialize_json(data: dict) -> ScoringStrategyConfig:
    out: ScoringStrategyConfig = {}  # type: ignore[typeddict-item]
    if data.get("defaultValue") is not None:
        import capo_eks.types.scoring_strategy

        out["default_value"] = capo_eks.types.scoring_strategy.deserialize_json(
            data["defaultValue"]
        )
    if data.get("constraints") is not None:
        import capo_eks.types.scoring_strategy_constraints

        out["constraints"] = (
            capo_eks.types.scoring_strategy_constraints.deserialize_json(
                data["constraints"]
            )
        )
    return out
