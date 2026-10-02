"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ResourceErrorCode``."""

from typing import Literal, TypeAlias, cast

"""<p>The error code.</p>"""
ResourceErrorCode: TypeAlias = Literal[
    "VALIDATION_ERROR",
    "INTERNAL_FAILURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ResourceErrorCode:
    return cast(ResourceErrorCode, data)
