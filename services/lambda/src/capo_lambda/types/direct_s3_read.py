"""Generated from Smithy shape ``com.amazonaws.lambda#DirectS3Read``."""

from typing import Literal, TypeAlias, cast

DirectS3Read: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: DirectS3Read) -> str:
    return value


def deserialize_json(data: str) -> DirectS3Read:
    return cast(DirectS3Read, data)
