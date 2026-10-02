"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectionRuleFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.detection_rule_filter

DetectionRuleFilterList: TypeAlias = list[
    "capo_guardduty.types.detection_rule_filter.DetectionRuleFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectionRuleFilterList) -> list:
    import capo_guardduty.types.detection_rule_filter

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.detection_rule_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> DetectionRuleFilterList:
    import capo_guardduty.types.detection_rule_filter

    out: DetectionRuleFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.detection_rule_filter.deserialize_json(item))
    return out
