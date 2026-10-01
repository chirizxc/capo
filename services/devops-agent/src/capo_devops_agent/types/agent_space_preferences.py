"""Generated from Smithy shape ``com.amazonaws.devopsagent#AgentSpacePreferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_preference_key

AgentSpacePreferences: TypeAlias = dict[
    "capo_devops_agent.types.agent_space_preference_key.AgentSpacePreferenceKey", "bool"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AgentSpacePreferences) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_devops_agent.types.agent_space_preference_key

        out[capo_devops_agent.types.agent_space_preference_key.serialize_json(key)] = (
            value
        )
    return out


def deserialize_json(data: dict) -> AgentSpacePreferences:
    out: AgentSpacePreferences = {}
    for key, value in data.items():
        import capo_devops_agent.types.agent_space_preference_key

        if value is None:
            continue
        out[
            capo_devops_agent.types.agent_space_preference_key.deserialize_json(key)
        ] = value
    return out
