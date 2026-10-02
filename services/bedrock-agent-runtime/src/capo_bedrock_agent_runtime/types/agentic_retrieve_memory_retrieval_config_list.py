"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMemoryRetrievalConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieval_config

AgenticRetrieveMemoryRetrievalConfigList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieval_config.AgenticRetrieveMemoryRetrievalConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMemoryRetrievalConfigList) -> list:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieval_config

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieval_config.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgenticRetrieveMemoryRetrievalConfigList:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieval_config

    out: AgenticRetrieveMemoryRetrievalConfigList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieval_config.deserialize_json(
                item
            )
        )
    return out
