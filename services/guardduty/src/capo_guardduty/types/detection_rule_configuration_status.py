"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectionRuleConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

DetectionRuleConfigurationStatus: TypeAlias = Literal[
    "ACTIVE",
    "PROCESSING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectionRuleConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> DetectionRuleConfigurationStatus:
    return cast(DetectionRuleConfigurationStatus, data)
