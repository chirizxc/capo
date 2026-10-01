"""Generated from Smithy shape ``com.amazonaws.geoplaces#GetPlaceAdditionalFeature``."""

from typing import Literal, TypeAlias, cast

GetPlaceAdditionalFeature: TypeAlias = Literal[
    "TimeZone",
    "Phonemes",
    "Access",
    "Contact",
    "SecondaryAddresses",
    "CrossReferences",
]


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaceAdditionalFeature) -> str:
    return value


def deserialize_json(data: str) -> GetPlaceAdditionalFeature:
    return cast(GetPlaceAdditionalFeature, data)
