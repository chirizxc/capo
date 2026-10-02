"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConnectorParameterOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.connector_parameter_override

ConnectorParameterOverrides: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.connector_parameter_override.ConnectorParameterOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorParameterOverrides) -> list:
    import capo_bedrock_agentcore_control.types.connector_parameter_override

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.connector_parameter_override.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConnectorParameterOverrides:
    import capo_bedrock_agentcore_control.types.connector_parameter_override

    out: ConnectorParameterOverrides = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.connector_parameter_override.deserialize_json(
                item
            )
        )
    return out
