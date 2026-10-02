"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveSourceRetrieverList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever

AgenticRetrieveSourceRetrieverList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever.AgenticRetrieveSourceRetriever"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveSourceRetrieverList) -> list:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgenticRetrieveSourceRetrieverList:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever

    out: AgenticRetrieveSourceRetrieverList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever.deserialize_json(
                item
            )
        )
    return out
