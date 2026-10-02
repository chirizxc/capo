"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMemoryRetrievalConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_list
    import capo_bedrock_agent_runtime.types.memory_namespace
    import capo_bedrock_agent_runtime.types.memory_strategy_id


class AgenticRetrieveMemoryRetrievalConfig(TypedDict, closed=True):
    namespace: NotRequired[
        "capo_bedrock_agent_runtime.types.memory_namespace.MemoryNamespace"
    ]
    """<p>The namespace prefix to filter memory records by. The agent retrieves memory records in namespaces that start with the provided prefix. You must specify either namespace or namespacePath.</p>"""
    namespace_path: NotRequired[
        "capo_bedrock_agent_runtime.types.memory_namespace.MemoryNamespace"
    ]
    """<p>The parent namespace to use for hierarchical retrievals. The agent retrieves all memory records whose namespace falls under the same parent hierarchy. You must specify either namespace or namespacePath.</p>"""
    strategy_id: NotRequired[
        "capo_bedrock_agent_runtime.types.memory_strategy_id.MemoryStrategyId"
    ]
    """<p>The extraction strategy ID that restricts retrieval to memory records produced by a single strategy. Omit this parameter to retrieve records from every strategy on the memory resource.</p>"""
    metadata_filters: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_list.AgenticRetrieveMemoryMetadataFilterList"
    ]
    """<p>The metadata filter expressions that restrict retrieval to matching memory records. You can specify a maximum of 5 expressions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMemoryRetrievalConfig) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "namespace_path" in value:
        out["namespacePath"] = value["namespace_path"]
    if "strategy_id" in value:
        out["strategyId"] = value["strategy_id"]
    if "metadata_filters" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_list

        out["metadataFilters"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_list.serialize_json(
                value["metadata_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgenticRetrieveMemoryRetrievalConfig:
    out: AgenticRetrieveMemoryRetrievalConfig = {}  # type: ignore[typeddict-item]
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("namespacePath") is not None:
        out["namespace_path"] = data["namespacePath"]
    if data.get("strategyId") is not None:
        out["strategy_id"] = data["strategyId"]
    if data.get("metadataFilters") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_list

        out["metadata_filters"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter_list.deserialize_json(
                data["metadataFilters"]
            )
        )
    return out
