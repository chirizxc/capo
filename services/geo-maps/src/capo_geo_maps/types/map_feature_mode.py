"""Generated from Smithy shape ``com.amazonaws.geomaps#MapFeatureMode``."""

from typing import Literal, TypeAlias, cast

MapFeatureMode: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: MapFeatureMode) -> str:
    return value


def deserialize_json(data: str) -> MapFeatureMode:
    return cast(MapFeatureMode, data)
