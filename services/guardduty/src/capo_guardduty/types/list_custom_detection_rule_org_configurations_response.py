"""Generated from Smithy shape ``com.amazonaws.guardduty#ListCustomDetectionRuleOrgConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detection_rule_org_configuration_summary_list
    import capo_guardduty.types.string


class ListCustomDetectionRuleOrgConfigurationsResponse(TypedDict, closed=True):
    configurations: NotRequired[
        "capo_guardduty.types.detection_rule_org_configuration_summary_list.DetectionRuleOrgConfigurationSummaryList"
    ]
    """<p>A list of organization configurations for custom detection rules.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>A pagination token to retrieve the next page of results. If this field is empty, there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomDetectionRuleOrgConfigurationsResponse) -> dict:
    out: dict = {}
    if "configurations" in value:
        import capo_guardduty.types.detection_rule_org_configuration_summary_list

        out["configurations"] = (
            capo_guardduty.types.detection_rule_org_configuration_summary_list.serialize_json(
                value["configurations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCustomDetectionRuleOrgConfigurationsResponse:
    out: ListCustomDetectionRuleOrgConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("configurations") is not None:
        import capo_guardduty.types.detection_rule_org_configuration_summary_list

        out["configurations"] = (
            capo_guardduty.types.detection_rule_org_configuration_summary_list.deserialize_json(
                data["configurations"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
