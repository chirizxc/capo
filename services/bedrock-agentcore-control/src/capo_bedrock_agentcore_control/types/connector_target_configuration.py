"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConnectorTargetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.connector_configurations
    import capo_bedrock_agentcore_control.types.connector_source
    import capo_bedrock_agentcore_control.types.enabled_connectors


class ConnectorTargetConfiguration(TypedDict, closed=True):
    source: "capo_bedrock_agentcore_control.types.connector_source.ConnectorSource"
    """<p>The source configuration identifying which connector to use.</p>"""
    enabled: NotRequired[
        "capo_bedrock_agentcore_control.types.enabled_connectors.EnabledConnectors"
    ]
    """<p>A list of tool names to enable from this connector. If absent, all tools provided by the connector are enabled.</p>"""
    configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.connector_configurations.ConnectorConfigurations"
    ]
    """<p>A list of per-tool configurations for the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorTargetConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.connector_source

    out["source"] = (
        capo_bedrock_agentcore_control.types.connector_source.serialize_json(
            value["source"]
        )
    )
    if "enabled" in value:
        import capo_bedrock_agentcore_control.types.enabled_connectors

        out["enabled"] = (
            capo_bedrock_agentcore_control.types.enabled_connectors.serialize_json(
                value["enabled"]
            )
        )
    if "configurations" in value:
        import capo_bedrock_agentcore_control.types.connector_configurations

        out["configurations"] = (
            capo_bedrock_agentcore_control.types.connector_configurations.serialize_json(
                value["configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorTargetConfiguration:
    out: ConnectorTargetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_bedrock_agentcore_control.types.connector_source

        out["source"] = (
            capo_bedrock_agentcore_control.types.connector_source.deserialize_json(
                data["source"]
            )
        )
    else:
        raise DeserializationError("ConnectorTargetConfiguration.source required")
    if data.get("enabled") is not None:
        import capo_bedrock_agentcore_control.types.enabled_connectors

        out["enabled"] = (
            capo_bedrock_agentcore_control.types.enabled_connectors.deserialize_json(
                data["enabled"]
            )
        )
    if data.get("configurations") is not None:
        import capo_bedrock_agentcore_control.types.connector_configurations

        out["configurations"] = (
            capo_bedrock_agentcore_control.types.connector_configurations.deserialize_json(
                data["configurations"]
            )
        )
    return out
