"""Generated from Smithy shape ``com.amazonaws.geoplaces#SuggestAdditionalFeature``."""

from typing import Literal, TypeAlias, cast

SuggestAdditionalFeature: TypeAlias = Literal[
    "Core",
    "TimeZone",
    "Phonemes",
    "Access",
    "CrossReferences",
]


# --- restJson1 ser/de ---
def serialize_json(value: SuggestAdditionalFeature) -> str:
    return value


def deserialize_json(data: str) -> SuggestAdditionalFeature:
    return cast(SuggestAdditionalFeature, data)
