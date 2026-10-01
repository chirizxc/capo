"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AgentRecommendationItemSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_recommendation_item_summary

AgentRecommendationItemSummaries: TypeAlias = list[
    "capo_wellarchitected.types.agent_recommendation_item_summary.AgentRecommendationItemSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentRecommendationItemSummaries) -> list:
    import capo_wellarchitected.types.agent_recommendation_item_summary

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.agent_recommendation_item_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgentRecommendationItemSummaries:
    import capo_wellarchitected.types.agent_recommendation_item_summary

    out: AgentRecommendationItemSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.agent_recommendation_item_summary.deserialize_json(
                item
            )
        )
    return out
