"""Generated from Smithy shape ``com.amazonaws.mq#SharedResourceErrorCode``."""

from typing import Literal, TypeAlias, cast

"""<p>The error code associated with the error.</p>"""
SharedResourceErrorCode: TypeAlias = Literal[
    "QUOTA_EXCEEDED",
    "SHARE_NOT_FOUND",
    "INVITE_FAILED",
    "SETUP_INCOMPLETE",
    "INTERNAL_ERROR",
    "AZ_MISMATCH",
    "RESOURCE_CONFIGURATION_NOT_FOUND",
]


# --- restJson1 ser/de ---
def serialize_json(value: SharedResourceErrorCode) -> str:
    return value


def deserialize_json(data: str) -> SharedResourceErrorCode:
    return cast(SharedResourceErrorCode, data)
