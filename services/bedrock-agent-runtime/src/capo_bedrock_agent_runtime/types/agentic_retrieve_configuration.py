"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_configuration
    import capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_model_type
    import capo_bedrock_agent_runtime.types.foundation_model_configuration
    import capo_bedrock_agent_runtime.types.foundation_model_type


class AgenticRetrieveConfiguration(TypedDict, closed=True):
    foundation_model_type: (
        "capo_bedrock_agent_runtime.types.foundation_model_type.FoundationModelType"
    )
    """<p>The type of foundation model to use. CUSTOM uses a specified model, MANAGED uses the service default.</p>"""
    foundation_model_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.foundation_model_configuration.FoundationModelConfiguration"
    ]
    """<p>The foundation model configuration. Required when foundationModelType is CUSTOM.</p>"""
    reranking_model_type: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_model_type.AgenticRetrieveRerankingModelType"
    ]
    """<p>The type of reranking model to use. CUSTOM uses a specified model, MANAGED uses the service default. If not specified, defaults to MANAGED for managed embedding knowledge bases and NONE for custom embedding knowledge bases.</p>"""
    reranking_configuration: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_configuration.AgenticRetrieveRerankingConfiguration"
    ]
    """<p>The reranking model configuration. Required when rerankingModelType is CUSTOM.</p>"""
    max_agent_iteration: "int"
    """<p>The maximum number of agent iterations for retrieval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.foundation_model_type

    out["foundationModelType"] = (
        capo_bedrock_agent_runtime.types.foundation_model_type.serialize_json(
            value.get("foundation_model_type", "MANAGED")
        )
    )
    if "foundation_model_configuration" in value:
        import capo_bedrock_agent_runtime.types.foundation_model_configuration

        out["foundationModelConfiguration"] = (
            capo_bedrock_agent_runtime.types.foundation_model_configuration.serialize_json(
                value["foundation_model_configuration"]
            )
        )
    if "reranking_model_type" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_model_type

        out["rerankingModelType"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_model_type.serialize_json(
                value["reranking_model_type"]
            )
        )
    if "reranking_configuration" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_configuration

        out["rerankingConfiguration"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_configuration.serialize_json(
                value["reranking_configuration"]
            )
        )
    out["maxAgentIteration"] = value.get("max_agent_iteration", 5)
    return out


def deserialize_json(data: dict) -> AgenticRetrieveConfiguration:
    out: AgenticRetrieveConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("foundationModelType") is not None:
        import capo_bedrock_agent_runtime.types.foundation_model_type

        out["foundation_model_type"] = (
            capo_bedrock_agent_runtime.types.foundation_model_type.deserialize_json(
                data["foundationModelType"]
            )
        )
    else:
        out["foundation_model_type"] = "MANAGED"
    if data.get("foundationModelConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.foundation_model_configuration

        out["foundation_model_configuration"] = (
            capo_bedrock_agent_runtime.types.foundation_model_configuration.deserialize_json(
                data["foundationModelConfiguration"]
            )
        )
    if data.get("rerankingModelType") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_model_type

        out["reranking_model_type"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_model_type.deserialize_json(
                data["rerankingModelType"]
            )
        )
    if data.get("rerankingConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_configuration

        out["reranking_configuration"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_reranking_configuration.deserialize_json(
                data["rerankingConfiguration"]
            )
        )
    if data.get("maxAgentIteration") is not None:
        out["max_agent_iteration"] = data["maxAgentIteration"]
    else:
        out["max_agent_iteration"] = 5
    return out
