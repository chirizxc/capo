"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DataSegmentErrorCode``."""

from typing import Literal, TypeAlias, cast

DataSegmentErrorCode: TypeAlias = Literal[
    "INTERNAL_FAILURE",
    "VALIDATION_ERROR",
    "RESOURCE_NOT_FOUND",
    "LIMIT_EXCEEDED",
    "CONFLICTING_OPERATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSegmentErrorCode) -> str:
    return value


def deserialize_json(data: str) -> DataSegmentErrorCode:
    return cast(DataSegmentErrorCode, data)
