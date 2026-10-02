"""Generated from Smithy shape ``com.amazonaws.connect#NotFoundBehaviorType``."""

from typing import Literal, TypeAlias, cast

NotFoundBehaviorType: TypeAlias = Literal[
    "USE_DEFAULT_VALUE",
    "OMIT",
]


# --- restJson1 ser/de ---
def serialize_json(value: NotFoundBehaviorType) -> str:
    return value


def deserialize_json(data: str) -> NotFoundBehaviorType:
    return cast(NotFoundBehaviorType, data)
