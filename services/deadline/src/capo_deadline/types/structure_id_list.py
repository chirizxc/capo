"""Generated from Smithy shape ``aws.cloudformation#StructureIdList``."""

from typing import TypeAlias

StructureIdList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: StructureIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> StructureIdList:
    return [item for item in data if item is not None]
