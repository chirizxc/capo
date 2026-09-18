"""Generated from Smithy shape ``com.amazonaws.devopsagent#Execution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.execution_status
    import capo_devops_agent.types.journal_timestamp


class Execution(TypedDict, closed=True):
    agent_space_id: "str"
    """<p>The unique identifier for the agent space containing this execution</p>"""
    execution_id: "str"
    """<p>The unique identifier for this execution</p>"""
    parent_execution_id: NotRequired["str"]
    """<p>The identifier of the parent execution, if this is a child execution</p>"""
    agent_sub_task: "str"
    """<p>The specific subtask being executed by the agent</p>"""
    created_at: "capo_devops_agent.types.journal_timestamp.JournalTimestamp"
    """<p>Timestamp when this execution was created</p>"""
    updated_at: "capo_devops_agent.types.journal_timestamp.JournalTimestamp"
    """<p>Timestamp when this execution was last updated</p>"""
    execution_status: "capo_devops_agent.types.execution_status.ExecutionStatus"
    """<p>The current status of this execution</p>"""
    agent_type: NotRequired["str"]
    """<p>The type of agent that performed this execution.</p>"""
    uid: NotRequired["str"]
    """<p>The unique identifier for the user session associated with this execution</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Execution) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["executionId"] = value["execution_id"]
    if "parent_execution_id" in value:
        out["parentExecutionId"] = value["parent_execution_id"]
    out["agentSubTask"] = value["agent_sub_task"]
    import capo_devops_agent.types.journal_timestamp

    out["createdAt"] = capo_devops_agent.types.journal_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_devops_agent.types.journal_timestamp

    out["updatedAt"] = capo_devops_agent.types.journal_timestamp.serialize_json(
        value["updated_at"]
    )
    import capo_devops_agent.types.execution_status

    out["executionStatus"] = capo_devops_agent.types.execution_status.serialize_json(
        value["execution_status"]
    )
    if "agent_type" in value:
        out["agentType"] = value["agent_type"]
    if "uid" in value:
        out["uid"] = value["uid"]
    return out


def deserialize_json(data: dict) -> Execution:
    out: Execution = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("Execution.agent_space_id required")
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("Execution.execution_id required")
    if data.get("parentExecutionId") is not None:
        out["parent_execution_id"] = data["parentExecutionId"]
    if data.get("agentSubTask") is not None:
        out["agent_sub_task"] = data["agentSubTask"]
    else:
        raise DeserializationError("Execution.agent_sub_task required")
    if data.get("createdAt") is not None:
        import capo_devops_agent.types.journal_timestamp

        out["created_at"] = capo_devops_agent.types.journal_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("Execution.created_at required")
    if data.get("updatedAt") is not None:
        import capo_devops_agent.types.journal_timestamp

        out["updated_at"] = capo_devops_agent.types.journal_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("Execution.updated_at required")
    if data.get("executionStatus") is not None:
        import capo_devops_agent.types.execution_status

        out["execution_status"] = (
            capo_devops_agent.types.execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    else:
        raise DeserializationError("Execution.execution_status required")
    if data.get("agentType") is not None:
        out["agent_type"] = data["agentType"]
    if data.get("uid") is not None:
        out["uid"] = data["uid"]
    return out
