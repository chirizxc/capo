"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveSourceMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_source_metadata

AgenticRetrieveSourceMetadataList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.agentic_retrieve_source_metadata.AgenticRetrieveSourceMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveSourceMetadataList) -> list:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_source_metadata

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_source_metadata.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgenticRetrieveSourceMetadataList:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_source_metadata

    out: AgenticRetrieveSourceMetadataList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_source_metadata.deserialize_json(
                item
            )
        )
    return out
