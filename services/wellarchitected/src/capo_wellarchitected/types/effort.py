"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Effort``."""

from typing import Literal, TypeAlias, cast

Effort: TypeAlias = Literal[
    "LARGE",
    "MEDIUM",
    "SMALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: Effort) -> str:
    return value


def deserialize_json(data: str) -> Effort:
    return cast(Effort, data)
