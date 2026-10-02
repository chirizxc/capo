"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveRerankingModelType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of reranking model.</p>"""
AgenticRetrieveRerankingModelType: TypeAlias = Literal[
    "CUSTOM",
    "MANAGED",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveRerankingModelType) -> str:
    return value


def deserialize_json(data: str) -> AgenticRetrieveRerankingModelType:
    return cast(AgenticRetrieveRerankingModelType, data)
