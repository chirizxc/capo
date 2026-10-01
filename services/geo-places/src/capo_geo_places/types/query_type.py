"""Generated from Smithy shape ``com.amazonaws.geoplaces#QueryType``."""

from typing import Literal, TypeAlias, cast

QueryType: TypeAlias = Literal[
    "Category",
    "BusinessChain",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryType) -> str:
    return value


def deserialize_json(data: str) -> QueryType:
    return cast(QueryType, data)
