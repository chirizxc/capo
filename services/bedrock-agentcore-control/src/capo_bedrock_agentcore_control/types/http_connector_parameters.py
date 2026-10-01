"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HttpConnectorParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.connector_parameter_name
    import capo_bedrock_agentcore_control.types.connector_parameter_value

HttpConnectorParameters: TypeAlias = dict[
    "capo_bedrock_agentcore_control.types.connector_parameter_name.ConnectorParameterName",
    "capo_bedrock_agentcore_control.types.connector_parameter_value.ConnectorParameterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: HttpConnectorParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> HttpConnectorParameters:
    out: HttpConnectorParameters = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
