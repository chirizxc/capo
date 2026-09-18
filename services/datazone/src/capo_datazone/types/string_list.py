"""Generated from Smithy shape ``com.amazonaws.datazone#StringList``."""

from typing import TypeAlias

StringList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: StringList) -> list:
    return list(value)


def deserialize_json(data: list) -> StringList:
    return [item for item in data if item is not None]
