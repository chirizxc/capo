"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveCitationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_citation

AgenticRetrieveCitationList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.agentic_retrieve_citation.AgenticRetrieveCitation"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveCitationList) -> list:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_citation

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_citation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgenticRetrieveCitationList:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_citation

    out: AgenticRetrieveCitationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_citation.deserialize_json(
                item
            )
        )
    return out
