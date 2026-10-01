"""Generated from Smithy shape ``com.amazonaws.geoplaces#PlaceType``."""

from typing import Literal, TypeAlias, cast

PlaceType: TypeAlias = Literal[
    "Country",
    "Region",
    "SubRegion",
    "Locality",
    "District",
    "SubDistrict",
    "PostalCode",
    "Block",
    "SubBlock",
    "Intersection",
    "Street",
    "PointOfInterest",
    "PointAddress",
    "InterpolatedAddress",
    "SecondaryAddress",
    "InferredSecondaryAddress",
]


# --- restJson1 ser/de ---
def serialize_json(value: PlaceType) -> str:
    return value


def deserialize_json(data: str) -> PlaceType:
    return cast(PlaceType, data)
