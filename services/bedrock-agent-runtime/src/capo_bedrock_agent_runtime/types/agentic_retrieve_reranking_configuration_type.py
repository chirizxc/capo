"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveRerankingConfigurationType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of reranking configuration.</p>"""
AgenticRetrieveRerankingConfigurationType: TypeAlias = Literal[
    "BEDROCK_RERANKING_MODEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveRerankingConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> AgenticRetrieveRerankingConfigurationType:
    return cast(AgenticRetrieveRerankingConfigurationType, data)
