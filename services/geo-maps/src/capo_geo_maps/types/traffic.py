"""Generated from Smithy shape ``com.amazonaws.geomaps#Traffic``."""

from typing import Literal, TypeAlias, cast

Traffic: TypeAlias = Literal[
    "All",
    "Congestion",
]


# --- restJson1 ser/de ---
def serialize_json(value: Traffic) -> str:
    return value


def deserialize_json(data: str) -> Traffic:
    return cast(Traffic, data)
