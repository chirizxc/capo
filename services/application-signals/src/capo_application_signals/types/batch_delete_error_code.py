"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchDeleteErrorCode``."""

from typing import Literal, TypeAlias, cast

"""Error codes for batch delete item-level failures."""
BatchDeleteErrorCode: TypeAlias = Literal[
    "ResourceNotFoundException",
    "AccessDeniedException",
    "InternalServiceException",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchDeleteErrorCode:
    return cast(BatchDeleteErrorCode, data)
