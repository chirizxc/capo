"""Generated from Smithy shape ``com.amazonaws.geomaps#Terrain``."""

from typing import Literal, TypeAlias, cast

Terrain: TypeAlias = Literal[
    "Hillshade",
    "Terrain3D",
]


# --- restJson1 ser/de ---
def serialize_json(value: Terrain) -> str:
    return value


def deserialize_json(data: str) -> Terrain:
    return cast(Terrain, data)
