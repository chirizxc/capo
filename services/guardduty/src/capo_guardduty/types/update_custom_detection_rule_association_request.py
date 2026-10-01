"""Generated from Smithy shape ``com.amazonaws.guardduty#UpdateCustomDetectionRuleAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.association_id
    import capo_guardduty.types.association_mode
    import capo_guardduty.types.rule_id


class UpdateCustomDetectionRuleAssociationRequest(TypedDict, closed=True):
    rule_id: "capo_guardduty.types.rule_id.RuleId"
    """<p>The unique identifier for the custom detection rule.</p>"""
    association_id: "capo_guardduty.types.association_id.AssociationId"
    """<p>The unique identifier for the association to update.</p>"""
    mode: NotRequired["capo_guardduty.types.association_mode.AssociationMode"]
    """<p>The rule execution mode. Valid values: <code>LIVE</code> | <code>DRY_RUN</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomDetectionRuleAssociationRequest) -> dict:
    out: dict = {}
    if "mode" in value:
        import capo_guardduty.types.association_mode

        out["mode"] = capo_guardduty.types.association_mode.serialize_json(
            value["mode"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCustomDetectionRuleAssociationRequest:
    out: UpdateCustomDetectionRuleAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("mode") is not None:
        import capo_guardduty.types.association_mode

        out["mode"] = capo_guardduty.types.association_mode.deserialize_json(
            data["mode"]
        )
    return out
