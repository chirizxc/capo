"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMemoryMetadataStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_string_list_item

AgenticRetrieveMemoryMetadataStringList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_string_list_item.AgenticRetrieveMemoryMetadataStringListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMemoryMetadataStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> AgenticRetrieveMemoryMetadataStringList:
    return [item for item in data if item is not None]
