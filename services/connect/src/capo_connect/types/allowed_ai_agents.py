"""Generated from Smithy shape ``com.amazonaws.connect#AllowedAIAgents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.ai_agent

AllowedAIAgents: TypeAlias = list["capo_connect.types.ai_agent.AIAgent"]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedAIAgents) -> list:
    import capo_connect.types.ai_agent

    out: list = []
    for item in value:
        out.append(capo_connect.types.ai_agent.serialize_json(item))
    return out


def deserialize_json(data: list) -> AllowedAIAgents:
    import capo_connect.types.ai_agent

    out: AllowedAIAgents = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.ai_agent.deserialize_json(item))
    return out
