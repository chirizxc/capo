"""Generated from Smithy shape ``com.amazonaws.securityagent#PrivateConnectionType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of a private connection, indicating whether it is service-managed or self-managed.</p>"""
PrivateConnectionType: TypeAlias = Literal[
    "SERVICE_MANAGED",
    "SELF_MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateConnectionType) -> str:
    return value


def deserialize_json(data: str) -> PrivateConnectionType:
    return cast(PrivateConnectionType, data)
