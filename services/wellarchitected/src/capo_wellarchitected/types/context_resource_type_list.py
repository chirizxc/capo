"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ContextResourceTypeList``."""

from typing import TypeAlias

ContextResourceTypeList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ContextResourceTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> ContextResourceTypeList:
    return [item for item in data if item is not None]
