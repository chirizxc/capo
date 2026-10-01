"""Generated from Smithy shape ``com.amazonaws.geoplaces#GeocodeAdditionalFeature``."""

from typing import Literal, TypeAlias, cast

GeocodeAdditionalFeature: TypeAlias = Literal[
    "TimeZone",
    "Access",
    "SecondaryAddresses",
    "Intersections",
]


# --- restJson1 ser/de ---
def serialize_json(value: GeocodeAdditionalFeature) -> str:
    return value


def deserialize_json(data: str) -> GeocodeAdditionalFeature:
    return cast(GeocodeAdditionalFeature, data)
