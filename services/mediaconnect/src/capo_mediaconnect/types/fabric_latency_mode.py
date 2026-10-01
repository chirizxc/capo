"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FabricLatencyMode``."""

from typing import Literal, TypeAlias, cast

FabricLatencyMode: TypeAlias = Literal[
    "BALANCED",
    "LOW_LATENCY",
]


# --- restJson1 ser/de ---
def serialize_json(value: FabricLatencyMode) -> str:
    return value


def deserialize_json(data: str) -> FabricLatencyMode:
    return cast(FabricLatencyMode, data)
