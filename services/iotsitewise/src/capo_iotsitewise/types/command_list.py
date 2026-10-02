"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CommandList``."""

from typing import TypeAlias

CommandList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: CommandList) -> list:
    return list(value)


def deserialize_json(data: list) -> CommandList:
    return [item for item in data if item is not None]
