"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchNearbyAdditionalFeature``."""

from typing import Literal, TypeAlias, cast

SearchNearbyAdditionalFeature: TypeAlias = Literal[
    "TimeZone",
    "Phonemes",
    "Access",
    "Contact",
    "CrossReferences",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchNearbyAdditionalFeature) -> str:
    return value


def deserialize_json(data: str) -> SearchNearbyAdditionalFeature:
    return cast(SearchNearbyAdditionalFeature, data)
