"""Generated from Smithy shape ``com.amazonaws.geomaps#TileAdditionalFeature``."""

from typing import Literal, TypeAlias, cast

TileAdditionalFeature: TypeAlias = Literal[
    "ContourLines",
    "Hillshade",
    "Logistics",
    "Transit",
]


# --- restJson1 ser/de ---
def serialize_json(value: TileAdditionalFeature) -> str:
    return value


def deserialize_json(data: str) -> TileAdditionalFeature:
    return cast(TileAdditionalFeature, data)
