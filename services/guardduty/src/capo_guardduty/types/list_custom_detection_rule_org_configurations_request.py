"""Generated from Smithy shape ``com.amazonaws.guardduty#ListCustomDetectionRuleOrgConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detection_rule_configuration_status
    import capo_guardduty.types.detection_rule_max_results
    import capo_guardduty.types.string


class ListCustomDetectionRuleOrgConfigurationsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_guardduty.types.detection_rule_max_results.DetectionRuleMaxResults"
    ]
    """<p>The maximum number of results to return in a single page. Minimum value of 1, maximum value of 100.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>A pagination token from a previous response. Use this token to retrieve the next page of results.</p>"""
    status: NotRequired[
        "capo_guardduty.types.detection_rule_configuration_status.DetectionRuleConfigurationStatus"
    ]
    """<p>The configuration status to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomDetectionRuleOrgConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCustomDetectionRuleOrgConfigurationsRequest:
    out: ListCustomDetectionRuleOrgConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
