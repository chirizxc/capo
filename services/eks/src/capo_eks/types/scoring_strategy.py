"""Generated from Smithy shape ``com.amazonaws.eks#ScoringStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.resource_weight_list
    import capo_eks.types.scoring_strategy_type


class ScoringStrategy(TypedDict, closed=True):
    type: NotRequired["capo_eks.types.scoring_strategy_type.ScoringStrategyType"]
    """<p>The scoring strategy type. Valid values are <code>LeastAllocated</code> or <code>MostAllocated</code>.</p>"""
    resources: NotRequired["capo_eks.types.resource_weight_list.ResourceWeightList"]
    """<p>The resource weights used for scoring nodes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScoringStrategy) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_eks.types.scoring_strategy_type

        out["type"] = capo_eks.types.scoring_strategy_type.serialize_json(value["type"])
    if "resources" in value:
        import capo_eks.types.resource_weight_list

        out["resources"] = capo_eks.types.resource_weight_list.serialize_json(
            value["resources"]
        )
    return out


def deserialize_json(data: dict) -> ScoringStrategy:
    out: ScoringStrategy = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_eks.types.scoring_strategy_type

        out["type"] = capo_eks.types.scoring_strategy_type.deserialize_json(
            data["type"]
        )
    if data.get("resources") is not None:
        import capo_eks.types.resource_weight_list

        out["resources"] = capo_eks.types.resource_weight_list.deserialize_json(
            data["resources"]
        )
    return out
