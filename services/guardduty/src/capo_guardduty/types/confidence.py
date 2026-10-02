"""Generated from Smithy shape ``com.amazonaws.guardduty#Confidence``."""

from typing import Literal, TypeAlias, cast

Confidence: TypeAlias = Literal[
    "Unknown",
    "Low",
    "Medium",
    "High",
]


# --- restJson1 ser/de ---
def serialize_json(value: Confidence) -> str:
    return value


def deserialize_json(data: str) -> Confidence:
    return cast(Confidence, data)
