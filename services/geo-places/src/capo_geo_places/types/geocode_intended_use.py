"""Generated from Smithy shape ``com.amazonaws.geoplaces#GeocodeIntendedUse``."""

from typing import Literal, TypeAlias, cast

GeocodeIntendedUse: TypeAlias = Literal[
    "SingleUse",
    "Storage",
]


# --- restJson1 ser/de ---
def serialize_json(value: GeocodeIntendedUse) -> str:
    return value


def deserialize_json(data: str) -> GeocodeIntendedUse:
    return cast(GeocodeIntendedUse, data)
