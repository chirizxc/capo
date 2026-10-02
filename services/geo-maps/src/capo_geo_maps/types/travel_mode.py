"""Generated from Smithy shape ``com.amazonaws.geomaps#TravelMode``."""

from typing import Literal, TypeAlias, cast

TravelMode: TypeAlias = Literal[
    "Transit",
    "Truck",
]


# --- restJson1 ser/de ---
def serialize_json(value: TravelMode) -> str:
    return value


def deserialize_json(data: str) -> TravelMode:
    return cast(TravelMode, data)
