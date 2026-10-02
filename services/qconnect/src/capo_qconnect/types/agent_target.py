"""Generated from Smithy shape ``com.amazonaws.qconnect#AgentTarget``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string


class _AgentTarget_aiAgentId(TypedDict, closed=True):
    aiAgentId: "capo_qconnect.types.non_empty_string.NonEmptyString"


class _AgentTarget_applicationId(TypedDict, closed=True):
    applicationId: "capo_qconnect.types.non_empty_string.NonEmptyString"


AgentTarget: TypeAlias = _AgentTarget_aiAgentId | _AgentTarget_applicationId


# --- restJson1 ser/de ---
def serialize_json(value: AgentTarget) -> dict:
    if "aiAgentId" in value:
        return {"aiAgentId": value["aiAgentId"]}
    elif "applicationId" in value:
        return {"applicationId": value["applicationId"]}
    else:
        raise SerializationError("AgentTarget: no variant present")


def deserialize_json(data: dict) -> AgentTarget:
    if data.get("aiAgentId") is not None:
        return {"aiAgentId": data["aiAgentId"]}
    elif data.get("applicationId") is not None:
        return {"applicationId": data["applicationId"]}
    else:
        raise DeserializationError("AgentTarget: no recognized variant key")
