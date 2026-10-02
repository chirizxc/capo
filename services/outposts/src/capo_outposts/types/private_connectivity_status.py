"""Generated from Smithy shape ``com.amazonaws.outposts#PrivateConnectivityStatus``."""

from typing import Literal, TypeAlias, cast

PrivateConnectivityStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateConnectivityStatus) -> str:
    return value


def deserialize_json(data: str) -> PrivateConnectivityStatus:
    return cast(PrivateConnectivityStatus, data)
