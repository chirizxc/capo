"""Generated from Smithy shape ``com.amazonaws.geoplaces#SuggestIntendedUse``."""

from typing import Literal, TypeAlias, cast

SuggestIntendedUse: TypeAlias = Literal["SingleUse",]


# --- restJson1 ser/de ---
def serialize_json(value: SuggestIntendedUse) -> str:
    return value


def deserialize_json(data: str) -> SuggestIntendedUse:
    return cast(SuggestIntendedUse, data)
