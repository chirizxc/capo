"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceQuickSightResourceType``."""

from typing import Literal, TypeAlias, cast

SpaceQuickSightResourceType: TypeAlias = Literal[
    "TOPIC",
    "DASHBOARD",
    "KNOWLEDGE_BASE",
    "ACTION_CONNECTOR",
    "DATA_SET",
]


# --- restJson1 ser/de ---
def serialize_json(value: SpaceQuickSightResourceType) -> str:
    return value


def deserialize_json(data: str) -> SpaceQuickSightResourceType:
    return cast(SpaceQuickSightResourceType, data)
