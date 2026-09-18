"""Generated from Smithy shape ``com.amazonaws.neptunedata#Classes``."""

from typing import TypeAlias

Classes: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: Classes) -> list:
    return list(value)


def deserialize_json(data: list) -> Classes:
    return [item for item in data if item is not None]
