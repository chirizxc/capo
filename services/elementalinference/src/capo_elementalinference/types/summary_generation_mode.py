"""Generated from Smithy shape ``com.amazonaws.elementalinference#SummaryGenerationMode``."""

from typing import Literal, TypeAlias, cast

SummaryGenerationMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SummaryGenerationMode) -> str:
    return value


def deserialize_json(data: str) -> SummaryGenerationMode:
    return cast(SummaryGenerationMode, data)
