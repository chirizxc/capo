"""Generated from Smithy shape ``com.amazonaws.geoplaces#GetPlaceIntendedUse``."""

from typing import Literal, TypeAlias, cast

GetPlaceIntendedUse: TypeAlias = Literal[
    "SingleUse",
    "Storage",
]


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaceIntendedUse) -> str:
    return value


def deserialize_json(data: str) -> GetPlaceIntendedUse:
    return cast(GetPlaceIntendedUse, data)
