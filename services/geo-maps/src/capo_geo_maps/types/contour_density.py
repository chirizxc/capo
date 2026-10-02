"""Generated from Smithy shape ``com.amazonaws.geomaps#ContourDensity``."""

from typing import Literal, TypeAlias, cast

ContourDensity: TypeAlias = Literal[
    "Low",
    "Medium",
    "High",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContourDensity) -> str:
    return value


def deserialize_json(data: str) -> ContourDensity:
    return cast(ContourDensity, data)
