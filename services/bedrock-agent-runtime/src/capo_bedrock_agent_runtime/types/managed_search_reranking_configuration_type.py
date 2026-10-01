"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ManagedSearchRerankingConfigurationType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of reranking configuration for managed search.</p>"""
ManagedSearchRerankingConfigurationType: TypeAlias = Literal["BEDROCK_RERANKING_MODEL",]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedSearchRerankingConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> ManagedSearchRerankingConfigurationType:
    return cast(ManagedSearchRerankingConfigurationType, data)
