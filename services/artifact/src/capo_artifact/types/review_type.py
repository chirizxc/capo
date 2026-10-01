"""Generated from Smithy shape ``com.amazonaws.artifact#ReviewType``."""

from typing import Literal, TypeAlias, cast

ReviewType: TypeAlias = Literal[
    "HUMAN",
    "AI",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReviewType) -> str:
    return value


def deserialize_json(data: str) -> ReviewType:
    return cast(ReviewType, data)
