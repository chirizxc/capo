"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentContextRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.uuid


class GetAgentContextRequest(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the profile containing the context.</p>"""
    id: "capo_wellarchitected.types.uuid.UUID"
    """<p>The unique identifier of the context to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentContextRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentContextRequest:
    out: GetAgentContextRequest = {}  # type: ignore[typeddict-item]
    return out
