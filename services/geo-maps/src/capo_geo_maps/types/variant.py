"""Generated from Smithy shape ``com.amazonaws.geomaps#Variant``."""

from typing import Literal, TypeAlias, cast

Variant: TypeAlias = Literal["Default",]


# --- restJson1 ser/de ---
def serialize_json(value: Variant) -> str:
    return value


def deserialize_json(data: str) -> Variant:
    return cast(Variant, data)
