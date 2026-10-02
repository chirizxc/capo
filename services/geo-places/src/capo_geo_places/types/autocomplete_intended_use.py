"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteIntendedUse``."""

from typing import Literal, TypeAlias, cast

AutocompleteIntendedUse: TypeAlias = Literal["SingleUse",]


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteIntendedUse) -> str:
    return value


def deserialize_json(data: str) -> AutocompleteIntendedUse:
    return cast(AutocompleteIntendedUse, data)
