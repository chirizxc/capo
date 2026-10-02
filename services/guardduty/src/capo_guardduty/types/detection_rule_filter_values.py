"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectionRuleFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.detection_rule_filter_value

DetectionRuleFilterValues: TypeAlias = list[
    "capo_guardduty.types.detection_rule_filter_value.DetectionRuleFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectionRuleFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> DetectionRuleFilterValues:
    return [item for item in data if item is not None]
