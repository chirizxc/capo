"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteFilterPlaceType``."""

from typing import Literal, TypeAlias, cast

AutocompleteFilterPlaceType: TypeAlias = Literal[
    "Locality",
    "PostalCode",
    "Street",
    "Intersection",
    "PointAddress",
    "InterpolatedAddress",
    "Country",
    "Region",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteFilterPlaceType) -> str:
    return value


def deserialize_json(data: str) -> AutocompleteFilterPlaceType:
    return cast(AutocompleteFilterPlaceType, data)
