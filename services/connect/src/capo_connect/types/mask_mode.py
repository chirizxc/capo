"""Generated from Smithy shape ``com.amazonaws.connect#MaskMode``."""

from typing import Literal, TypeAlias, cast

MaskMode: TypeAlias = Literal[
    "PII",
    "EntityType",
]


# --- restJson1 ser/de ---
def serialize_json(value: MaskMode) -> str:
    return value


def deserialize_json(data: str) -> MaskMode:
    return cast(MaskMode, data)
