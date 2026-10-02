"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#NamespaceAllowedValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.namespace_allowed_value

NamespaceAllowedValuesList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.namespace_allowed_value.NamespaceAllowedValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: NamespaceAllowedValuesList) -> list:
    return list(value)


def deserialize_json(data: list) -> NamespaceAllowedValuesList:
    return [item for item in data if item is not None]
