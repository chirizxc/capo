"""Generated from Smithy shape ``com.amazonaws.geoplaces#PlaceAttribute``."""

from typing import Literal, TypeAlias, cast

PlaceAttribute: TypeAlias = Literal["DriveThrough",]


# --- restJson1 ser/de ---
def serialize_json(value: PlaceAttribute) -> str:
    return value


def deserialize_json(data: str) -> PlaceAttribute:
    return cast(PlaceAttribute, data)
