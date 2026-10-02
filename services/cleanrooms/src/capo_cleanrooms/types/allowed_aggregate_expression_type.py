"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AllowedAggregateExpressionType``."""

from typing import Literal, TypeAlias, cast

AllowedAggregateExpressionType: TypeAlias = Literal[
    "COLUMNS_ONLY",
    "ANY_EXPRESSION",
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedAggregateExpressionType) -> str:
    return value


def deserialize_json(data: str) -> AllowedAggregateExpressionType:
    return cast(AllowedAggregateExpressionType, data)
