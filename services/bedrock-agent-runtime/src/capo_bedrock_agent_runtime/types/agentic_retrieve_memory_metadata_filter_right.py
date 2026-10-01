"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMemoryMetadataFilterRight``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_value


class _AgenticRetrieveMemoryMetadataFilterRight_metadataValue(TypedDict, closed=True):
    metadataValue: "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_value.AgenticRetrieveMemoryMetadataValue"


AgenticRetrieveMemoryMetadataFilterRight: TypeAlias = (
    _AgenticRetrieveMemoryMetadataFilterRight_metadataValue
)


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMemoryMetadataFilterRight) -> dict:
    if "metadataValue" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_value

        return {
            "metadataValue": capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_value.serialize_json(
                value["metadataValue"]
            )
        }
    else:
        raise SerializationError(
            "AgenticRetrieveMemoryMetadataFilterRight: no variant present"
        )


def deserialize_json(data: dict) -> AgenticRetrieveMemoryMetadataFilterRight:
    if data.get("metadataValue") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_value

        return {
            "metadataValue": capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_value.deserialize_json(
                data["metadataValue"]
            )
        }
    else:
        raise DeserializationError(
            "AgenticRetrieveMemoryMetadataFilterRight: no recognized variant key"
        )
