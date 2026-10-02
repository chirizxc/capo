"""Generated from Smithy shape ``com.amazonaws.synthetics#LocationType``."""

from typing import Literal, TypeAlias, cast

LocationType: TypeAlias = Literal[
    "Primary",
    "Replica",
]


# --- restJson1 ser/de ---
def serialize_json(value: LocationType) -> str:
    return value


def deserialize_json(data: str) -> LocationType:
    return cast(LocationType, data)
