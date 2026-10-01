"""Generated from Smithy shape ``com.amazonaws.geomaps#ScaleBarUnit``."""

from typing import Literal, TypeAlias, cast

ScaleBarUnit: TypeAlias = Literal[
    "Kilometers",
    "KilometersMiles",
    "Miles",
    "MilesKilometers",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScaleBarUnit) -> str:
    return value


def deserialize_json(data: str) -> ScaleBarUnit:
    return cast(ScaleBarUnit, data)
