"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentRecommendationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_recommendation_arn
    import capo_wellarchitected.types.remediation_type


class GetAgentRecommendationRequest(TypedDict, closed=True):
    recommendation_arn: (
        "capo_wellarchitected.types.agent_recommendation_arn.AgentRecommendationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the recommendation to retrieve.</p>"""
    remediation_type: NotRequired[
        "capo_wellarchitected.types.remediation_type.RemediationType"
    ]
    """<p>Optional filter on remediation type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentRecommendationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentRecommendationRequest:
    out: GetAgentRecommendationRequest = {}  # type: ignore[typeddict-item]
    return out
