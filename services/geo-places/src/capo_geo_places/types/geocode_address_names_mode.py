"""Generated from Smithy shape ``com.amazonaws.geoplaces#GeocodeAddressNamesMode``."""

from typing import Literal, TypeAlias, cast

GeocodeAddressNamesMode: TypeAlias = Literal[
    "Matched",
    "Administrative",
]


# --- restJson1 ser/de ---
def serialize_json(value: GeocodeAddressNamesMode) -> str:
    return value


def deserialize_json(data: str) -> GeocodeAddressNamesMode:
    return cast(GeocodeAddressNamesMode, data)
