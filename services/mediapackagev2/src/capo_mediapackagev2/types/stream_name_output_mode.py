"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#StreamNameOutputMode``."""

from typing import Literal, TypeAlias, cast

StreamNameOutputMode: TypeAlias = Literal[
    "INDEX",
    "PASSTHROUGH_NAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamNameOutputMode) -> str:
    return value


def deserialize_json(data: str) -> StreamNameOutputMode:
    return cast(StreamNameOutputMode, data)
