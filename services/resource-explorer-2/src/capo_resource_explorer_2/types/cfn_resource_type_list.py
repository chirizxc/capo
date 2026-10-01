"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#CFNResourceTypeList``."""

from typing import TypeAlias

CFNResourceTypeList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: CFNResourceTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> CFNResourceTypeList:
    return [item for item in data if item is not None]
