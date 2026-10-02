"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#NamespaceKeysList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.namespace_key_entry

NamespaceKeysList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.namespace_key_entry.NamespaceKeyEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: NamespaceKeysList) -> list:
    import capo_bedrock_agentcore_control.types.namespace_key_entry

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.namespace_key_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NamespaceKeysList:
    import capo_bedrock_agentcore_control.types.namespace_key_entry

    out: NamespaceKeysList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.namespace_key_entry.deserialize_json(
                item
            )
        )
    return out
