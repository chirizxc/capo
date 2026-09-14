"""Generated from Smithy shape ``com.amazonaws.sustainability#DimensionValueList``."""

from typing import TypeAlias

DimensionValueList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> DimensionValueList:
    return [item for item in data if item is not None]
