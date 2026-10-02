"""Generated from Smithy shape ``com.amazonaws.imagebuilder#RegionFailureStatus``."""

from typing import Literal, TypeAlias, cast

RegionFailureStatus: TypeAlias = Literal[
    "FAILED",
    "CANCELLED",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: RegionFailureStatus) -> str:
    return value


def deserialize_json(data: str) -> RegionFailureStatus:
    return cast(RegionFailureStatus, data)
