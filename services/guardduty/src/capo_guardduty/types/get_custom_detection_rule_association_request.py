"""Generated from Smithy shape ``com.amazonaws.guardduty#GetCustomDetectionRuleAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.association_id
    import capo_guardduty.types.rule_id


class GetCustomDetectionRuleAssociationRequest(TypedDict, closed=True):
    rule_id: "capo_guardduty.types.rule_id.RuleId"
    """<p>The unique identifier for the custom detection rule.</p>"""
    association_id: "capo_guardduty.types.association_id.AssociationId"
    """<p>The unique identifier for the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomDetectionRuleAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCustomDetectionRuleAssociationRequest:
    out: GetCustomDetectionRuleAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
