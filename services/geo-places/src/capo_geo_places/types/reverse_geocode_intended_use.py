"""Generated from Smithy shape ``com.amazonaws.geoplaces#ReverseGeocodeIntendedUse``."""

from typing import Literal, TypeAlias, cast

ReverseGeocodeIntendedUse: TypeAlias = Literal[
    "SingleUse",
    "Storage",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReverseGeocodeIntendedUse) -> str:
    return value


def deserialize_json(data: str) -> ReverseGeocodeIntendedUse:
    return cast(ReverseGeocodeIntendedUse, data)
