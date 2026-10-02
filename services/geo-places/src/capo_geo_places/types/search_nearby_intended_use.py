"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchNearbyIntendedUse``."""

from typing import Literal, TypeAlias, cast

SearchNearbyIntendedUse: TypeAlias = Literal[
    "SingleUse",
    "Storage",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchNearbyIntendedUse) -> str:
    return value


def deserialize_json(data: str) -> SearchNearbyIntendedUse:
    return cast(SearchNearbyIntendedUse, data)
