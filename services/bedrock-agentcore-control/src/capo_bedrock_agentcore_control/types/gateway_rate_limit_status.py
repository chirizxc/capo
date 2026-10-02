"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayRateLimitStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a gateway limit.</p>"""
GatewayRateLimitStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRateLimitStatus) -> str:
    return value


def deserialize_json(data: str) -> GatewayRateLimitStatus:
    return cast(GatewayRateLimitStatus, data)
