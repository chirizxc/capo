"""Generated from Smithy shape ``com.amazonaws.connect#PerformanceCategoryName``."""

from typing import Literal, TypeAlias, cast

PerformanceCategoryName: TypeAlias = Literal[
    "NEEDS_IMPROVEMENT",
    "EXCEEDS_EXPECTATIONS",
]


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceCategoryName) -> str:
    return value


def deserialize_json(data: str) -> PerformanceCategoryName:
    return cast(PerformanceCategoryName, data)
