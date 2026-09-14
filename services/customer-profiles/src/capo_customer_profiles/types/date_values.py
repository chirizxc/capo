"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DateValues``."""

from typing import TypeAlias

DateValues: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: DateValues) -> list:
    return list(value)


def deserialize_json(data: list) -> DateValues:
    return [item for item in data if item is not None]
