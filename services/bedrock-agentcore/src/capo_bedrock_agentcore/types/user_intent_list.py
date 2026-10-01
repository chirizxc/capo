"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#UserIntentList``."""

from typing import TypeAlias

UserIntentList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: UserIntentList) -> list:
    return list(value)


def deserialize_json(data: list) -> UserIntentList:
    return [item for item in data if item is not None]
