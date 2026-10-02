"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InferenceConnectorTargetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.inference_connector_source


class InferenceConnectorTargetConfiguration(TypedDict, closed=True):
    source: "capo_bedrock_agentcore_control.types.inference_connector_source.InferenceConnectorSource"
    """<p>The source configuration identifying which inference connector to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceConnectorTargetConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.inference_connector_source

    out["source"] = (
        capo_bedrock_agentcore_control.types.inference_connector_source.serialize_json(
            value["source"]
        )
    )
    return out


def deserialize_json(data: dict) -> InferenceConnectorTargetConfiguration:
    out: InferenceConnectorTargetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_bedrock_agentcore_control.types.inference_connector_source

        out["source"] = (
            capo_bedrock_agentcore_control.types.inference_connector_source.deserialize_json(
                data["source"]
            )
        )
    else:
        raise DeserializationError(
            "InferenceConnectorTargetConfiguration.source required"
        )
    return out
