"""Generated from Smithy shape ``com.amazonaws.backup#AccessPointStatus``."""

from typing import Literal, TypeAlias, cast

AccessPointStatus: TypeAlias = Literal[
    "AVAILABLE",
    "CREATING",
    "DELETING",
    "DISASSOCIATED",
    "DISASSOCIATING",
    "EXPIRED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessPointStatus) -> str:
    return value


def deserialize_json(data: str) -> AccessPointStatus:
    return cast(AccessPointStatus, data)
