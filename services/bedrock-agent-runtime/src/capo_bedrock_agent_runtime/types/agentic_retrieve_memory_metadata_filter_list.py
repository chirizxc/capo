"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMemoryMetadataFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter

AgenticRetrieveMemoryMetadataFilterList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter.AgenticRetrieveMemoryMetadataFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMemoryMetadataFilterList) -> list:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgenticRetrieveMemoryMetadataFilterList:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter

    out: AgenticRetrieveMemoryMetadataFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_filter.deserialize_json(
                item
            )
        )
    return out
