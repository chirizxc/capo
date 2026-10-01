"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConnectorConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.connector_configuration

ConnectorConfigurations: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.connector_configuration.ConnectorConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorConfigurations) -> list:
    import capo_bedrock_agentcore_control.types.connector_configuration

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.connector_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConnectorConfigurations:
    import capo_bedrock_agentcore_control.types.connector_configuration

    out: ConnectorConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.connector_configuration.deserialize_json(
                item
            )
        )
    return out
