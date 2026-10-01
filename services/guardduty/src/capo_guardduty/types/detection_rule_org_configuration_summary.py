"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectionRuleOrgConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.association_mode
    import capo_guardduty.types.detection_rule_configuration_status
    import capo_guardduty.types.rule_id
    import capo_guardduty.types.string
    import capo_guardduty.types.timestamp


class DetectionRuleOrgConfigurationSummary(TypedDict, closed=True):
    rule_id: NotRequired["capo_guardduty.types.rule_id.RuleId"]
    """<p>The unique identifier for the custom detection rule.</p>"""
    mode: NotRequired["capo_guardduty.types.association_mode.AssociationMode"]
    """<p>The rule execution mode.</p>"""
    status: NotRequired[
        "capo_guardduty.types.detection_rule_configuration_status.DetectionRuleConfigurationStatus"
    ]
    """<p>The configuration status.</p>"""
    status_reason: NotRequired["capo_guardduty.types.string.String"]
    """<p>The reason for the current configuration status.</p>"""
    created_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the organization configuration was created.</p>"""
    updated_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the organization configuration was last updated.</p>"""
    expires_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the organization configuration expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectionRuleOrgConfigurationSummary) -> dict:
    out: dict = {}
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    if "mode" in value:
        import capo_guardduty.types.association_mode

        out["mode"] = capo_guardduty.types.association_mode.serialize_json(
            value["mode"]
        )
    if "status" in value:
        import capo_guardduty.types.detection_rule_configuration_status

        out["status"] = (
            capo_guardduty.types.detection_rule_configuration_status.serialize_json(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
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


def deserialize_json(data: dict) -> DetectionRuleOrgConfigurationSummary:
    out: DetectionRuleOrgConfigurationSummary = {}  # type: ignore[typeddict-item]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    if data.get("mode") is not None:
        import capo_guardduty.types.association_mode

        out["mode"] = capo_guardduty.types.association_mode.deserialize_json(
            data["mode"]
        )
    if data.get("status") is not None:
        import capo_guardduty.types.detection_rule_configuration_status

        out["status"] = (
            capo_guardduty.types.detection_rule_configuration_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
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
