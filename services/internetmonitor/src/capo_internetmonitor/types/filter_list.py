"""Generated from Smithy shape ``com.amazonaws.internetmonitor#FilterList``."""

from typing import TypeAlias

FilterList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterList:
    return [item for item in data if item is not None]
