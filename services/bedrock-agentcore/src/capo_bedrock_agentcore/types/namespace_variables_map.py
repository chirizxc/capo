"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#NamespaceVariablesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.namespace_variable_name
    import capo_bedrock_agentcore.types.namespace_variable_value

NamespaceVariablesMap: TypeAlias = dict[
    "capo_bedrock_agentcore.types.namespace_variable_name.NamespaceVariableName",
    "capo_bedrock_agentcore.types.namespace_variable_value.NamespaceVariableValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: NamespaceVariablesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> NamespaceVariablesMap:
    out: NamespaceVariablesMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
