"""Generated from Smithy shape ``com.amazonaws.devopsagent#ToolClassification``."""

from typing import Literal, TypeAlias, cast

ToolClassification: TypeAlias = Literal[
    "READ_ONLY",
    "MUTATIVE",
    "DESTRUCTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ToolClassification) -> str:
    return value


def deserialize_json(data: str) -> ToolClassification:
    return cast(ToolClassification, data)
