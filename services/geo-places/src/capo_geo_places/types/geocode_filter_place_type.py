"""Generated from Smithy shape ``com.amazonaws.geoplaces#GeocodeFilterPlaceType``."""

from typing import Literal, TypeAlias, cast

GeocodeFilterPlaceType: TypeAlias = Literal[
    "Locality",
    "PostalCode",
    "Intersection",
    "Street",
    "PointAddress",
    "InterpolatedAddress",
    "SecondaryAddress",
    "PointOfInterest",
    "Country",
    "Region",
]


# --- restJson1 ser/de ---
def serialize_json(value: GeocodeFilterPlaceType) -> str:
    return value


def deserialize_json(data: str) -> GeocodeFilterPlaceType:
    return cast(GeocodeFilterPlaceType, data)
