"""Generated from Smithy shape ``com.amazonaws.guardduty#DeleteCustomDetectionRuleAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.association_id
    import capo_guardduty.types.rule_id


class DeleteCustomDetectionRuleAssociationRequest(TypedDict, closed=True):
    rule_id: "capo_guardduty.types.rule_id.RuleId"
    """<p>The unique identifier for the custom detection rule.</p>"""
    association_id: "capo_guardduty.types.association_id.AssociationId"
    """<p>The unique identifier for the association to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomDetectionRuleAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCustomDetectionRuleAssociationRequest:
    out: DeleteCustomDetectionRuleAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
