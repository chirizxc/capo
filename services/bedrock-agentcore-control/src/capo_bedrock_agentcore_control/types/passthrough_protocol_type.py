"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PassthroughProtocolType``."""

from typing import Literal, TypeAlias, cast

PassthroughProtocolType: TypeAlias = Literal[
    "MCP",
    "A2A",
    "INFERENCE",
    "CUSTOM",
]


# --- restJson1 ser/de ---
def serialize_json(value: PassthroughProtocolType) -> str:
    return value


def deserialize_json(data: str) -> PassthroughProtocolType:
    return cast(PassthroughProtocolType, data)
