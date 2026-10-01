"""Generated from Smithy shape ``com.amazonaws.securityagent#PrivateConnectionStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a private connection.</p>"""
PrivateConnectionStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateConnectionStatus) -> str:
    return value


def deserialize_json(data: str) -> PrivateConnectionStatus:
    return cast(PrivateConnectionStatus, data)
