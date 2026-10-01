"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DeleteAgentGoalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.uuid


class DeleteAgentGoalRequest(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the profile containing the goal.</p>"""
    id: "capo_wellarchitected.types.uuid.UUID"
    """<p>The unique identifier of the goal to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentGoalRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAgentGoalRequest:
    out: DeleteAgentGoalRequest = {}  # type: ignore[typeddict-item]
    return out
