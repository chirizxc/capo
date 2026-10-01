"""Generated from Smithy shape ``com.amazonaws.guardduty#ListCustomDetectionRuleAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.association_mode
    import capo_guardduty.types.detection_rule_max_results
    import capo_guardduty.types.rule_id
    import capo_guardduty.types.string


class ListCustomDetectionRuleAssociationsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_guardduty.types.detection_rule_max_results.DetectionRuleMaxResults"
    ]
    """<p>The maximum number of results to return in a single page. Minimum value of 1, maximum value of 100.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>A pagination token from a previous response. Use this token to retrieve the next page of results.</p>"""
    rule_id: NotRequired["capo_guardduty.types.rule_id.RuleId"]
    """<p>The unique identifier for the custom detection rule to filter associations by.</p>"""
    mode: NotRequired["capo_guardduty.types.association_mode.AssociationMode"]
    """<p>The rule execution mode to filter associations by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomDetectionRuleAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCustomDetectionRuleAssociationsRequest:
    out: ListCustomDetectionRuleAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
