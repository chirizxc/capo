"""Generated from Smithy shape ``com.amazonaws.geoplaces#AccessPointType``."""

from typing import Literal, TypeAlias, cast

AccessPointType: TypeAlias = Literal[
    "Delivery",
    "Emergency",
    "Entrance",
    "Loading",
    "Other",
    "Parking",
    "Taxi",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessPointType) -> str:
    return value


def deserialize_json(data: str) -> AccessPointType:
    return cast(AccessPointType, data)
