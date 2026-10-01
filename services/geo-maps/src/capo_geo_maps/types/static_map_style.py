"""Generated from Smithy shape ``com.amazonaws.geomaps#StaticMapStyle``."""

from typing import Literal, TypeAlias, cast

StaticMapStyle: TypeAlias = Literal[
    "Satellite",
    "Standard",
]


# --- restJson1 ser/de ---
def serialize_json(value: StaticMapStyle) -> str:
    return value


def deserialize_json(data: str) -> StaticMapStyle:
    return cast(StaticMapStyle, data)
