"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchTextIntendedUse``."""

from typing import Literal, TypeAlias, cast

SearchTextIntendedUse: TypeAlias = Literal[
    "SingleUse",
    "Storage",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchTextIntendedUse) -> str:
    return value


def deserialize_json(data: str) -> SearchTextIntendedUse:
    return cast(SearchTextIntendedUse, data)
