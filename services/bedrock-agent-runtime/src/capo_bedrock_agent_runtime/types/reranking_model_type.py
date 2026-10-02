"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankingModelType``."""

from typing import Literal, TypeAlias, cast

RerankingModelType: TypeAlias = Literal[
    "CUSTOM",
    "MANAGED",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RerankingModelType) -> str:
    return value


def deserialize_json(data: str) -> RerankingModelType:
    return cast(RerankingModelType, data)
