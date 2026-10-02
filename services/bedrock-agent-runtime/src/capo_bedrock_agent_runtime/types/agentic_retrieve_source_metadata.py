"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveSourceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_type


class AgenticRetrieveSourceMetadata(TypedDict, closed=True):
    identifier: NotRequired["str"]
    """<p>The identifier of the retrieval source.</p>"""
    retrieval_type: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_type.AgenticRetrieveType"
    ]
    """<p>The type of retrieval source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveSourceMetadata) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "retrieval_type" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_type

        out["retrievalType"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_type.serialize_json(
                value["retrieval_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgenticRetrieveSourceMetadata:
    out: AgenticRetrieveSourceMetadata = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    if data.get("retrievalType") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_type

        out["retrieval_type"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_type.deserialize_json(
                data["retrievalType"]
            )
        )
    return out
