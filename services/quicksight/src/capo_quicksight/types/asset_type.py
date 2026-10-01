"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetType``."""

from typing import Literal, TypeAlias, cast

AssetType: TypeAlias = Literal[
    "AGENT",
    "SPACE",
    "KNOWLEDGE_BASE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetType) -> str:
    return value


def deserialize_json(data: str) -> AssetType:
    return cast(AssetType, data)
