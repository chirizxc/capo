"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DeleteAgentProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn


class DeleteAgentProfileRequest(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the profile to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAgentProfileRequest:
    out: DeleteAgentProfileRequest = {}  # type: ignore[typeddict-item]
    return out
