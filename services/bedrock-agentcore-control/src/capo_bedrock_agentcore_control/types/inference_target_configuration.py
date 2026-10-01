"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InferenceTargetConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.inference_connector_target_configuration
    import capo_bedrock_agentcore_control.types.inference_provider_target_configuration


class _InferenceTargetConfiguration_connector(TypedDict, closed=True):
    connector: "capo_bedrock_agentcore_control.types.inference_connector_target_configuration.InferenceConnectorTargetConfiguration"


class _InferenceTargetConfiguration_provider(TypedDict, closed=True):
    provider: "capo_bedrock_agentcore_control.types.inference_provider_target_configuration.InferenceProviderTargetConfiguration"


InferenceTargetConfiguration: TypeAlias = (
    _InferenceTargetConfiguration_connector | _InferenceTargetConfiguration_provider
)


# --- restJson1 ser/de ---
def serialize_json(value: InferenceTargetConfiguration) -> dict:
    if "connector" in value:
        import capo_bedrock_agentcore_control.types.inference_connector_target_configuration

        return {
            "connector": capo_bedrock_agentcore_control.types.inference_connector_target_configuration.serialize_json(
                value["connector"]
            )
        }
    elif "provider" in value:
        import capo_bedrock_agentcore_control.types.inference_provider_target_configuration

        return {
            "provider": capo_bedrock_agentcore_control.types.inference_provider_target_configuration.serialize_json(
                value["provider"]
            )
        }
    else:
        raise SerializationError("InferenceTargetConfiguration: no variant present")


def deserialize_json(data: dict) -> InferenceTargetConfiguration:
    if data.get("connector") is not None:
        import capo_bedrock_agentcore_control.types.inference_connector_target_configuration

        return {
            "connector": capo_bedrock_agentcore_control.types.inference_connector_target_configuration.deserialize_json(
                data["connector"]
            )
        }
    elif data.get("provider") is not None:
        import capo_bedrock_agentcore_control.types.inference_provider_target_configuration

        return {
            "provider": capo_bedrock_agentcore_control.types.inference_provider_target_configuration.deserialize_json(
                data["provider"]
            )
        }
    else:
        raise DeserializationError(
            "InferenceTargetConfiguration: no recognized variant key"
        )
