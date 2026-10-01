"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ContextAwsServiceList``."""

from typing import TypeAlias

ContextAwsServiceList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ContextAwsServiceList) -> list:
    return list(value)


def deserialize_json(data: list) -> ContextAwsServiceList:
    return [item for item in data if item is not None]
