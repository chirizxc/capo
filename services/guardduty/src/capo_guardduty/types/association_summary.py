"""Generated from Smithy shape ``com.amazonaws.guardduty#AssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.association_id
    import capo_guardduty.types.association_mode
    import capo_guardduty.types.detection_rule_arn
    import capo_guardduty.types.rule_id
    import capo_guardduty.types.timestamp


class AssociationSummary(TypedDict, closed=True):
    association_id: NotRequired["capo_guardduty.types.association_id.AssociationId"]
    """<p>The unique identifier for the association.</p>"""
    arn: NotRequired["capo_guardduty.types.detection_rule_arn.DetectionRuleArn"]
    """<p>The Amazon Resource Name (ARN) of the association.</p>"""
    rule_id: NotRequired["capo_guardduty.types.rule_id.RuleId"]
    """<p>The unique identifier for the custom detection rule.</p>"""
    mode: NotRequired["capo_guardduty.types.association_mode.AssociationMode"]
    """<p>The rule execution mode. Valid values: <code>LIVE</code> | <code>DRY_RUN</code>.</p>"""
    created_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the association was created.</p>"""
    updated_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the association was last updated.</p>"""
    expires_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the association expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociationSummary) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["associationId"] = value["association_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    if "mode" in value:
        import capo_guardduty.types.association_mode

        out["mode"] = capo_guardduty.types.association_mode.serialize_json(
            value["mode"]
        )
    if "created_at" in value:
        import capo_guardduty.types.timestamp

        out["createdAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_guardduty.types.timestamp

        out["updatedAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "expires_at" in value:
        import capo_guardduty.types.timestamp

        out["expiresAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["expires_at"]
        )
    return out


def deserialize_json(data: dict) -> AssociationSummary:
    out: AssociationSummary = {}  # type: ignore[typeddict-item]
    if data.get("associationId") is not None:
        out["association_id"] = data["associationId"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    if data.get("mode") is not None:
        import capo_guardduty.types.association_mode

        out["mode"] = capo_guardduty.types.association_mode.deserialize_json(
            data["mode"]
        )
    if data.get("createdAt") is not None:
        import capo_guardduty.types.timestamp

        out["created_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_guardduty.types.timestamp

        out["updated_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("expiresAt") is not None:
        import capo_guardduty.types.timestamp

        out["expires_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["expiresAt"]
        )
    return out
