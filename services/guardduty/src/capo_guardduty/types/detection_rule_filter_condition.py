"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectionRuleFilterCondition``."""

from typing import Literal, TypeAlias, cast

DetectionRuleFilterCondition: TypeAlias = Literal[
    "EQUALS",
    "CONTAINS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectionRuleFilterCondition) -> str:
    return value


def deserialize_json(data: str) -> DetectionRuleFilterCondition:
    return cast(DetectionRuleFilterCondition, data)
