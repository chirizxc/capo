"""Generated from Smithy shape ``com.amazonaws.geomaps#PoiDensity``."""

from typing import Literal, TypeAlias, cast

PoiDensity: TypeAlias = Literal[
    "Off",
    "VerySparse",
    "Sparse",
    "Default",
    "Dense",
    "VeryDense",
]


# --- restJson1 ser/de ---
def serialize_json(value: PoiDensity) -> str:
    return value


def deserialize_json(data: str) -> PoiDensity:
    return cast(PoiDensity, data)
