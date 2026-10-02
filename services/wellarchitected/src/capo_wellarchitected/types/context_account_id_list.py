"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ContextAccountIdList``."""

from typing import TypeAlias

ContextAccountIdList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ContextAccountIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ContextAccountIdList:
    return [item for item in data if item is not None]
