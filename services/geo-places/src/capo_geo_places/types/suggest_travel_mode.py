"""Generated from Smithy shape ``com.amazonaws.geoplaces#SuggestTravelMode``."""

from typing import Literal, TypeAlias, cast

SuggestTravelMode: TypeAlias = Literal[
    "Car",
    "Scooter",
    "Truck",
]


# --- restJson1 ser/de ---
def serialize_json(value: SuggestTravelMode) -> str:
    return value


def deserialize_json(data: str) -> SuggestTravelMode:
    return cast(SuggestTravelMode, data)
