"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteAdditionalFeature``."""

from typing import Literal, TypeAlias, cast

AutocompleteAdditionalFeature: TypeAlias = Literal["Core",]


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteAdditionalFeature) -> str:
    return value


def deserialize_json(data: str) -> AutocompleteAdditionalFeature:
    return cast(AutocompleteAdditionalFeature, data)
