"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#SpekeVersion``."""

from typing import Literal, TypeAlias, cast

SpekeVersion: TypeAlias = Literal[
    "V2_0",
    "V2_1",
]


# --- restJson1 ser/de ---
def serialize_json(value: SpekeVersion) -> str:
    return value


def deserialize_json(data: str) -> SpekeVersion:
    return cast(SpekeVersion, data)
