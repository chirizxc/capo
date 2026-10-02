"""Generated from Smithy shape ``com.amazonaws.geoplaces#ReverseGeocodeAdditionalFeature``."""

from typing import Literal, TypeAlias, cast

ReverseGeocodeAdditionalFeature: TypeAlias = Literal[
    "TimeZone",
    "Access",
    "Intersections",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReverseGeocodeAdditionalFeature) -> str:
    return value


def deserialize_json(data: str) -> ReverseGeocodeAdditionalFeature:
    return cast(ReverseGeocodeAdditionalFeature, data)
