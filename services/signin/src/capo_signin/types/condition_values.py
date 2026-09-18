"""Generated from Smithy shape ``com.amazonaws.signin#ConditionValues``."""

from typing import TypeAlias

ConditionValues: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ConditionValues) -> list:
    return list(value)


def deserialize_json(data: list) -> ConditionValues:
    return [item for item in data if item is not None]
