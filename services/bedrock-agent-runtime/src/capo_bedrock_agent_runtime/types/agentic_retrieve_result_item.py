"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_metadata
    import capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever
    import capo_bedrock_agent_runtime.types.retrieval_content


class AgenticRetrieveResultItem(TypedDict, closed=True):
    content: "capo_bedrock_agent_runtime.types.retrieval_content.RetrievalContent"
    """<p>The retrieved content.</p>"""
    metadata: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_metadata.AgenticRetrieveMetadata"
    ]
    """<p>Metadata associated with the retrieved item.</p>"""
    source_retriever: "capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever.AgenticRetrieveSourceRetriever"
    """<p>The source retriever that produced this result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveResultItem) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.retrieval_content

    out["content"] = capo_bedrock_agent_runtime.types.retrieval_content.serialize_json(
        value["content"]
    )
    if "metadata" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_metadata

        out["metadata"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_metadata.serialize_json(
                value["metadata"]
            )
        )
    import capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever

    out["sourceRetriever"] = (
        capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever.serialize_json(
            value["source_retriever"]
        )
    )
    return out


def deserialize_json(data: dict) -> AgenticRetrieveResultItem:
    out: AgenticRetrieveResultItem = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        import capo_bedrock_agent_runtime.types.retrieval_content

        out["content"] = (
            capo_bedrock_agent_runtime.types.retrieval_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("AgenticRetrieveResultItem.content required")
    if data.get("metadata") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_metadata

        out["metadata"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_metadata.deserialize_json(
                data["metadata"]
            )
        )
    if data.get("sourceRetriever") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever

        out["source_retriever"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever.deserialize_json(
                data["sourceRetriever"]
            )
        )
    else:
        raise DeserializationError(
            "AgenticRetrieveResultItem.source_retriever required"
        )
    return out
