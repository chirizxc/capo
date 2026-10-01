"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of retrieval source.</p>"""
AgenticRetrieveType: TypeAlias = Literal[
    "BedrockKnowledgeBase",
    "BedrockAgentCoreMemory",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveType) -> str:
    return value


def deserialize_json(data: str) -> AgenticRetrieveType:
    return cast(AgenticRetrieveType, data)
