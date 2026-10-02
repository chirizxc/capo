"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ShaderCacheStatus``."""

from typing import Literal, TypeAlias, cast

ShaderCacheStatus: TypeAlias = Literal[
    "INITIALIZED",
    "PROCESSING",
    "READY",
    "DELETING",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: ShaderCacheStatus) -> str:
    return value


def deserialize_json(data: str) -> ShaderCacheStatus:
    return cast(ShaderCacheStatus, data)
