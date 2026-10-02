"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DimensionKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.dimension_key

DimensionKeys: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.dimension_key.DimensionKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionKeys) -> list:
    return list(value)


def deserialize_json(data: list) -> DimensionKeys:
    return [item for item in data if item is not None]
