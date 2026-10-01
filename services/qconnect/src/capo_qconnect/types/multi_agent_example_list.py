"""Generated from Smithy shape ``com.amazonaws.qconnect#MultiAgentExampleList``."""

from typing import TypeAlias

MultiAgentExampleList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: MultiAgentExampleList) -> list:
    return list(value)


def deserialize_json(data: list) -> MultiAgentExampleList:
    return [item for item in data if item is not None]
