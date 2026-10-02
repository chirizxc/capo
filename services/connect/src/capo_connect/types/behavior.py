"""Generated from Smithy shape ``com.amazonaws.connect#Behavior``."""

from typing import Literal, TypeAlias, cast

Behavior: TypeAlias = Literal[
    "Enable",
    "Disable",
]


# --- restJson1 ser/de ---
def serialize_json(value: Behavior) -> str:
    return value


def deserialize_json(data: str) -> Behavior:
    return cast(Behavior, data)
