"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn


class GetAgentProfileRequest(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the optimization profile to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentProfileRequest:
    out: GetAgentProfileRequest = {}  # type: ignore[typeddict-item]
    return out
