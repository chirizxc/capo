"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TargetType``."""

from typing import Literal, TypeAlias, cast

TargetType: TypeAlias = Literal[
    "OPEN_API_SCHEMA",
    "SMITHY_MODEL",
    "MCP_SERVER",
    "LAMBDA",
    "API_GATEWAY",
    "CONNECTOR",
    "AGENTCORE_RUNTIME",
    "PASSTHROUGH",
    "PROVIDER",
    "HTTP_CONNECTOR",
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetType) -> str:
    return value


def deserialize_json(data: str) -> TargetType:
    return cast(TargetType, data)
