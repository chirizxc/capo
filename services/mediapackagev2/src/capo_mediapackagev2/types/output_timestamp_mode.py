"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#OutputTimestampMode``."""

from typing import Literal, TypeAlias, cast

OutputTimestampMode: TypeAlias = Literal[
    "PASSTHROUGH",
    "REBASED_TO_CHANNEL_START",
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputTimestampMode) -> str:
    return value


def deserialize_json(data: str) -> OutputTimestampMode:
    return cast(OutputTimestampMode, data)
