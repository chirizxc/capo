"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectionRuleSeverity``."""

from typing import Literal, TypeAlias, cast

DetectionRuleSeverity: TypeAlias = Literal[
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectionRuleSeverity) -> str:
    return value


def deserialize_json(data: str) -> DetectionRuleSeverity:
    return cast(DetectionRuleSeverity, data)
