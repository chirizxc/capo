"""Generated from Smithy shape ``com.amazonaws.geoplaces#ReverseGeocodeFilterPlaceType``."""

from typing import Literal, TypeAlias, cast

ReverseGeocodeFilterPlaceType: TypeAlias = Literal[
    "Locality",
    "Intersection",
    "Street",
    "PointAddress",
    "InterpolatedAddress",
    "SecondaryAddress",
    "PointOfInterest",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReverseGeocodeFilterPlaceType) -> str:
    return value


def deserialize_json(data: str) -> ReverseGeocodeFilterPlaceType:
    return cast(ReverseGeocodeFilterPlaceType, data)
