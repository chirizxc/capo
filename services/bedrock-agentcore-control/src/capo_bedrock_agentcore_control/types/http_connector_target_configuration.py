"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HttpConnectorTargetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.http_connector_parameters
    import capo_bedrock_agentcore_control.types.http_connector_source


class HttpConnectorTargetConfiguration(TypedDict, closed=True):
    source: (
        "capo_bedrock_agentcore_control.types.http_connector_source.HttpConnectorSource"
    )
    """<p>The source configuration identifying which HTTP connector to use.</p>"""
    parameters: NotRequired[
        "capo_bedrock_agentcore_control.types.http_connector_parameters.HttpConnectorParameters"
    ]
    """<p>The resource parameters for this connector (for example, <code>memoryId</code>). The service validates these parameters against the request path at runtime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpConnectorTargetConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.http_connector_source

    out["source"] = (
        capo_bedrock_agentcore_control.types.http_connector_source.serialize_json(
            value["source"]
        )
    )
    if "parameters" in value:
        import capo_bedrock_agentcore_control.types.http_connector_parameters

        out["parameters"] = (
            capo_bedrock_agentcore_control.types.http_connector_parameters.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> HttpConnectorTargetConfiguration:
    out: HttpConnectorTargetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_bedrock_agentcore_control.types.http_connector_source

        out["source"] = (
            capo_bedrock_agentcore_control.types.http_connector_source.deserialize_json(
                data["source"]
            )
        )
    else:
        raise DeserializationError("HttpConnectorTargetConfiguration.source required")
    if data.get("parameters") is not None:
        import capo_bedrock_agentcore_control.types.http_connector_parameters

        out["parameters"] = (
            capo_bedrock_agentcore_control.types.http_connector_parameters.deserialize_json(
                data["parameters"]
            )
        )
    return out
