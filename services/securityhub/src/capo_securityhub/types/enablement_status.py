"""Generated from Smithy shape ``com.amazonaws.securityhub#EnablementStatus``."""

from typing import Literal, TypeAlias, cast

EnablementStatus: TypeAlias = Literal[
    "ENABLED",
    "PENDING_ENABLEMENT",
    "FAILED_TO_ENABLE",
    "PENDING_UPDATE",
    "FAILED_TO_UPDATE",
    "PENDING_DELETION",
    "FAILED_TO_DELETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EnablementStatus) -> str:
    return value


def deserialize_json(data: str) -> EnablementStatus:
    return cast(EnablementStatus, data)
