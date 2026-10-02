"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ContextRegionList``."""

from typing import TypeAlias

ContextRegionList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ContextRegionList) -> list:
    return list(value)


def deserialize_json(data: list) -> ContextRegionList:
    return [item for item in data if item is not None]
