"""Generated from Smithy shape ``com.amazonaws.inspector2#EnablementStatus``."""

from typing import Literal, TypeAlias, cast

EnablementStatus: TypeAlias = Literal[
    "ENABLED",
    "PENDING_ENABLEMENT",
    "FAILED_TO_ENABLE",
    "PENDING_UPDATE",
    "FAILED_TO_UPDATE",
    "PENDING_DELETION",
    "DELETED",
    "FAILED_TO_DELETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EnablementStatus) -> str:
    return value


def deserialize_json(data: str) -> EnablementStatus:
    return cast(EnablementStatus, data)
