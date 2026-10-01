"""Generated from Smithy shape ``com.amazonaws.artifact#InputSource``."""

from typing import Literal, TypeAlias, cast

InputSource: TypeAlias = Literal[
    "TEXT",
    "FILE",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputSource) -> str:
    return value


def deserialize_json(data: str) -> InputSource:
    return cast(InputSource, data)
