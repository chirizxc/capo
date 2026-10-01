"""Generated from Smithy shape ``com.amazonaws.vpclattice#ProtocolType``."""

from typing import Literal, TypeAlias, cast

ProtocolType: TypeAlias = Literal[
    "TCP",
    "TCP_UDP",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProtocolType) -> str:
    return value


def deserialize_json(data: str) -> ProtocolType:
    return cast(ProtocolType, data)
