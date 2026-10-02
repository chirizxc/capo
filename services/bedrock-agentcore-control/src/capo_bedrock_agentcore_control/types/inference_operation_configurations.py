"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InferenceOperationConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.inference_operation_configuration

InferenceOperationConfigurations: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.inference_operation_configuration.InferenceOperationConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: InferenceOperationConfigurations) -> list:
    import capo_bedrock_agentcore_control.types.inference_operation_configuration

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.inference_operation_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InferenceOperationConfigurations:
    import capo_bedrock_agentcore_control.types.inference_operation_configuration

    out: InferenceOperationConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.inference_operation_configuration.deserialize_json(
                item
            )
        )
    return out
