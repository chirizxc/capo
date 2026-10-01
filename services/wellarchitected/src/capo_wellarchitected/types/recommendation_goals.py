"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RecommendationGoals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.recommendation_goal

RecommendationGoals: TypeAlias = list[
    "capo_wellarchitected.types.recommendation_goal.RecommendationGoal"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationGoals) -> list:
    import capo_wellarchitected.types.recommendation_goal

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.recommendation_goal.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendationGoals:
    import capo_wellarchitected.types.recommendation_goal

    out: RecommendationGoals = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.recommendation_goal.deserialize_json(item)
        )
    return out
