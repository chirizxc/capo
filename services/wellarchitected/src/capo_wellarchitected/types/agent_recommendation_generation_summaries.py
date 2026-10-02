"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AgentRecommendationGenerationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_recommendation_generation_summary

AgentRecommendationGenerationSummaries: TypeAlias = list[
    "capo_wellarchitected.types.agent_recommendation_generation_summary.AgentRecommendationGenerationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentRecommendationGenerationSummaries) -> list:
    import capo_wellarchitected.types.agent_recommendation_generation_summary

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.agent_recommendation_generation_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgentRecommendationGenerationSummaries:
    import capo_wellarchitected.types.agent_recommendation_generation_summary

    out: AgentRecommendationGenerationSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.agent_recommendation_generation_summary.deserialize_json(
                item
            )
        )
    return out
