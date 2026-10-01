"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModelEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.model_entry

ModelEntries: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.model_entry.ModelEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelEntries) -> list:
    import capo_bedrock_agentcore_control.types.model_entry

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.model_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ModelEntries:
    import capo_bedrock_agentcore_control.types.model_entry

    out: ModelEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.model_entry.deserialize_json(item)
        )
    return out
