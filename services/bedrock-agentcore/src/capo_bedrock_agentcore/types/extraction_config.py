"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExtractionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.namespace_variables_map


class ExtractionConfig(TypedDict, closed=True):
    namespace_variables: NotRequired[
        "capo_bedrock_agentcore.types.namespace_variables_map.NamespaceVariablesMap"
    ]
    """<p>A map of <code>namespaceKeys</code> to their values. The service substitutes these values into <code>namespaceTemplates</code> during long-term memory extraction to control namespace hierarchy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionConfig) -> dict:
    out: dict = {}
    if "namespace_variables" in value:
        import capo_bedrock_agentcore.types.namespace_variables_map

        out["namespaceVariables"] = (
            capo_bedrock_agentcore.types.namespace_variables_map.serialize_json(
                value["namespace_variables"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExtractionConfig:
    out: ExtractionConfig = {}  # type: ignore[typeddict-item]
    if data.get("namespaceVariables") is not None:
        import capo_bedrock_agentcore.types.namespace_variables_map

        out["namespace_variables"] = (
            capo_bedrock_agentcore.types.namespace_variables_map.deserialize_json(
                data["namespaceVariables"]
            )
        )
    return out
