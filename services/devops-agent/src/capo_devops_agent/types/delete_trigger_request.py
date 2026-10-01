"""Generated from Smithy shape ``com.amazonaws.devopsagent#DeleteTriggerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_identifier
    import capo_devops_agent.types.resource_id


class DeleteTriggerRequest(TypedDict, closed=True):
    agent_space_id: (
        "capo_devops_agent.types.agent_space_identifier.AgentSpaceIdentifier"
    )
    """<p>The unique identifier for the agent space containing the Trigger</p>"""
    trigger_id: "capo_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the Trigger to delete</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTriggerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTriggerRequest:
    out: DeleteTriggerRequest = {}  # type: ignore[typeddict-item]
    return out
