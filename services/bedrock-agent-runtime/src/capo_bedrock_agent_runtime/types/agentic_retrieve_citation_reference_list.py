"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveCitationReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_citation_reference

AgenticRetrieveCitationReferenceList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.agentic_retrieve_citation_reference.AgenticRetrieveCitationReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveCitationReferenceList) -> list:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_citation_reference

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_citation_reference.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgenticRetrieveCitationReferenceList:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_citation_reference

    out: AgenticRetrieveCitationReferenceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_citation_reference.deserialize_json(
                item
            )
        )
    return out
