"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchTextAdditionalFeature``."""

from typing import Literal, TypeAlias, cast

SearchTextAdditionalFeature: TypeAlias = Literal[
    "TimeZone",
    "Phonemes",
    "Access",
    "Contact",
    "CrossReferences",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchTextAdditionalFeature) -> str:
    return value


def deserialize_json(data: str) -> SearchTextAdditionalFeature:
    return cast(SearchTextAdditionalFeature, data)
