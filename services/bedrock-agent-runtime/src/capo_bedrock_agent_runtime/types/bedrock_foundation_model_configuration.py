"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#BedrockFoundationModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.bedrock_foundation_model_model_configuration


class BedrockFoundationModelConfiguration(TypedDict, closed=True):
    model_configuration: "capo_bedrock_agent_runtime.types.bedrock_foundation_model_model_configuration.BedrockFoundationModelModelConfiguration"
    """<p>The model configuration containing the model ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockFoundationModelConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.bedrock_foundation_model_model_configuration

    out["modelConfiguration"] = (
        capo_bedrock_agent_runtime.types.bedrock_foundation_model_model_configuration.serialize_json(
            value["model_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> BedrockFoundationModelConfiguration:
    out: BedrockFoundationModelConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("modelConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.bedrock_foundation_model_model_configuration

        out["model_configuration"] = (
            capo_bedrock_agent_runtime.types.bedrock_foundation_model_model_configuration.deserialize_json(
                data["modelConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "BedrockFoundationModelConfiguration.model_configuration required"
        )
    return out
