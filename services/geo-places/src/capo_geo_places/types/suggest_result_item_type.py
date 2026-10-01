"""Generated from Smithy shape ``com.amazonaws.geoplaces#SuggestResultItemType``."""

from typing import Literal, TypeAlias, cast

SuggestResultItemType: TypeAlias = Literal[
    "Place",
    "Query",
]


# --- restJson1 ser/de ---
def serialize_json(value: SuggestResultItemType) -> str:
    return value


def deserialize_json(data: str) -> SuggestResultItemType:
    return cast(SuggestResultItemType, data)
