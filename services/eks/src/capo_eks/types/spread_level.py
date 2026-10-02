"""Generated from Smithy shape ``com.amazonaws.eks#SpreadLevel``."""

from typing import Literal, TypeAlias, cast

SpreadLevel: TypeAlias = Literal[
    "host",
    "rack",
]


# --- restJson1 ser/de ---
def serialize_json(value: SpreadLevel) -> str:
    return value


def deserialize_json(data: str) -> SpreadLevel:
    return cast(SpreadLevel, data)
