"""Generated from Smithy shape ``com.amazonaws.mq#SharedResourceStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the shared resource.</p>"""
SharedResourceStatus: TypeAlias = Literal[
    "AVAILABLE",
    "SETUP_IN_PROGRESS",
    "DELETION_IN_PROGRESS",
    "PENDING_CREATE",
    "PENDING_DELETE",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: SharedResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> SharedResourceStatus:
    return cast(SharedResourceStatus, data)
