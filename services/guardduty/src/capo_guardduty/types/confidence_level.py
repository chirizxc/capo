"""Generated from Smithy shape ``com.amazonaws.guardduty#ConfidenceLevel``."""

from typing import Literal, TypeAlias, cast

ConfidenceLevel: TypeAlias = Literal[
    "HIGH",
    "MEDIUM",
    "LOW",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfidenceLevel) -> str:
    return value


def deserialize_json(data: str) -> ConfidenceLevel:
    return cast(ConfidenceLevel, data)
