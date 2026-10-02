"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectionRuleOrgConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.detection_rule_org_configuration_summary

DetectionRuleOrgConfigurationSummaryList: TypeAlias = list[
    "capo_guardduty.types.detection_rule_org_configuration_summary.DetectionRuleOrgConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectionRuleOrgConfigurationSummaryList) -> list:
    import capo_guardduty.types.detection_rule_org_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_guardduty.types.detection_rule_org_configuration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DetectionRuleOrgConfigurationSummaryList:
    import capo_guardduty.types.detection_rule_org_configuration_summary

    out: DetectionRuleOrgConfigurationSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_guardduty.types.detection_rule_org_configuration_summary.deserialize_json(
                item
            )
        )
    return out
