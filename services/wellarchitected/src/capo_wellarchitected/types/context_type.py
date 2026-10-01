"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ContextType``."""

from typing import Literal, TypeAlias, cast

ContextType: TypeAlias = Literal["APPLICATION",]


# --- restJson1 ser/de ---
def serialize_json(value: ContextType) -> str:
    return value


def deserialize_json(data: str) -> ContextType:
    return cast(ContextType, data)
