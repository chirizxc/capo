"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentRecommendationGenerationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.uuid


class GetAgentRecommendationGenerationRequest(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The ARN of the optimization profile associated with this generation.</p>"""
    generation_id: "capo_wellarchitected.types.uuid.UUID"
    """<p>The unique identifier of the recommendation generation to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentRecommendationGenerationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentRecommendationGenerationRequest:
    out: GetAgentRecommendationGenerationRequest = {}  # type: ignore[typeddict-item]
    return out
