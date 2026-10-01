"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#OutputLockingMode``."""

from typing import Literal, TypeAlias, cast

OutputLockingMode: TypeAlias = Literal[
    "EPOCH_LOCKED",
    "NON_EPOCH_LOCKED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputLockingMode) -> str:
    return value


def deserialize_json(data: str) -> OutputLockingMode:
    return cast(OutputLockingMode, data)
