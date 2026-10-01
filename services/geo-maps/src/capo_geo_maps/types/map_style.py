"""Generated from Smithy shape ``com.amazonaws.geomaps#MapStyle``."""

from typing import Literal, TypeAlias, cast

MapStyle: TypeAlias = Literal[
    "Standard",
    "Monochrome",
    "Hybrid",
    "Satellite",
]


# --- restJson1 ser/de ---
def serialize_json(value: MapStyle) -> str:
    return value


def deserialize_json(data: str) -> MapStyle:
    return cast(MapStyle, data)
