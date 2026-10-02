"""Generated from Smithy shape ``com.amazonaws.medialive#OutputUsage``."""

from typing import Literal, TypeAlias, cast

"""Output Usage"""
OutputUsage: TypeAlias = Literal[
    "MULTIVIEW_EQUAL_SIZE_VIEW",
    "MULTIVIEW_PRIMARY_VIEW",
    "MULTIVIEW_SECONDARY_VIEW",
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputUsage) -> str:
    return value


def deserialize_json(data: str) -> OutputUsage:
    return cast(OutputUsage, data)
