"""Generated from Smithy shape ``com.amazonaws.securityhub#DiscoveryType``."""

from typing import Literal, TypeAlias, cast

DiscoveryType: TypeAlias = Literal[
    "Managed",
    "SelfHosted",
]


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveryType) -> str:
    return value


def deserialize_json(data: str) -> DiscoveryType:
    return cast(DiscoveryType, data)
