"""Generated from Smithy shape ``com.amazonaws.geoplaces#TypePlacement``."""

from typing import Literal, TypeAlias, cast

TypePlacement: TypeAlias = Literal[
    "BeforeBaseName",
    "AfterBaseName",
]


# --- restJson1 ser/de ---
def serialize_json(value: TypePlacement) -> str:
    return value


def deserialize_json(data: str) -> TypePlacement:
    return cast(TypePlacement, data)
