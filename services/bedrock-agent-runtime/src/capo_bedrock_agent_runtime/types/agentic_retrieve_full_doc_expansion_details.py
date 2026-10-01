"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveFullDocExpansionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever


class AgenticRetrieveFullDocExpansionDetails(TypedDict, closed=True):
    document_id: NotRequired["str"]
    """<p>The identifier of the document to expand.</p>"""
    source_retriever: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever.AgenticRetrieveSourceRetriever"
    ]
    """<p>The source retriever associated with the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveFullDocExpansionDetails) -> dict:
    out: dict = {}
    if "document_id" in value:
        out["documentId"] = value["document_id"]
    if "source_retriever" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever

        out["sourceRetriever"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever.serialize_json(
                value["source_retriever"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgenticRetrieveFullDocExpansionDetails:
    out: AgenticRetrieveFullDocExpansionDetails = {}  # type: ignore[typeddict-item]
    if data.get("documentId") is not None:
        out["document_id"] = data["documentId"]
    if data.get("sourceRetriever") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever

        out["source_retriever"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_source_retriever.deserialize_json(
                data["sourceRetriever"]
            )
        )
    return out
