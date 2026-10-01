"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchTextTravelMode``."""

from typing import Literal, TypeAlias, cast

SearchTextTravelMode: TypeAlias = Literal[
    "Car",
    "Scooter",
    "Truck",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchTextTravelMode) -> str:
    return value


def deserialize_json(data: str) -> SearchTextTravelMode:
    return cast(SearchTextTravelMode, data)
