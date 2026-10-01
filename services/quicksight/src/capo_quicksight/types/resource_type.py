"""Generated from Smithy shape ``com.amazonaws.quicksight#ResourceType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of resource that a limit applies to.</p>"""
ResourceType: TypeAlias = Literal[
    "INDEX_STORAGE",
    "AGENT_HOURS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    return cast(ResourceType, data)
