"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateTriggerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_identifier
    import capo_devops_agent.types.resource_id
    import capo_devops_agent.types.trigger_status


class UpdateTriggerRequest(TypedDict, closed=True):
    agent_space_id: (
        "capo_devops_agent.types.agent_space_identifier.AgentSpaceIdentifier"
    )
    """<p>The unique identifier for the agent space containing the Trigger</p>"""
    trigger_id: "capo_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the Trigger to update</p>"""
    status: NotRequired["capo_devops_agent.types.trigger_status.TriggerStatus"]
    """<p>The new status for the Trigger</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier used for idempotent Trigger update</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTriggerRequest) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateTriggerRequest:
    out: UpdateTriggerRequest = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
