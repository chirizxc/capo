"""Generated from Smithy shape ``com.amazonaws.guardduty#UpdateCustomDetectionRuleOrgConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.association_mode
    import capo_guardduty.types.detection_rule_account_ids
    import capo_guardduty.types.rule_id


class UpdateCustomDetectionRuleOrgConfigurationRequest(TypedDict, closed=True):
    rule_id: "capo_guardduty.types.rule_id.RuleId"
    """<p>The unique identifier for the custom detection rule.</p>"""
    mode: NotRequired["capo_guardduty.types.association_mode.AssociationMode"]
    """<p>The execution mode of the organization configuration. Valid values: <code>LIVE</code> | <code>DRY_RUN</code>.</p>"""
    include_account_ids: NotRequired[
        "capo_guardduty.types.detection_rule_account_ids.DetectionRuleAccountIds"
    ]
    """<p>The account IDs to include in the organization configuration. Mutually exclusive with <code>ExcludeAccountIds</code>.</p>"""
    exclude_account_ids: NotRequired[
        "capo_guardduty.types.detection_rule_account_ids.DetectionRuleAccountIds"
    ]
    """<p>The account IDs to exclude from the organization configuration. Mutually exclusive with <code>IncludeAccountIds</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomDetectionRuleOrgConfigurationRequest) -> dict:
    out: dict = {}
    if "mode" in value:
        import capo_guardduty.types.association_mode

        out["mode"] = capo_guardduty.types.association_mode.serialize_json(
            value["mode"]
        )
    if "include_account_ids" in value:
        import capo_guardduty.types.detection_rule_account_ids

        out["includeAccountIds"] = (
            capo_guardduty.types.detection_rule_account_ids.serialize_json(
                value["include_account_ids"]
            )
        )
    if "exclude_account_ids" in value:
        import capo_guardduty.types.detection_rule_account_ids

        out["excludeAccountIds"] = (
            capo_guardduty.types.detection_rule_account_ids.serialize_json(
                value["exclude_account_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCustomDetectionRuleOrgConfigurationRequest:
    out: UpdateCustomDetectionRuleOrgConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("mode") is not None:
        import capo_guardduty.types.association_mode

        out["mode"] = capo_guardduty.types.association_mode.deserialize_json(
            data["mode"]
        )
    if data.get("includeAccountIds") is not None:
        import capo_guardduty.types.detection_rule_account_ids

        out["include_account_ids"] = (
            capo_guardduty.types.detection_rule_account_ids.deserialize_json(
                data["includeAccountIds"]
            )
        )
    if data.get("excludeAccountIds") is not None:
        import capo_guardduty.types.detection_rule_account_ids

        out["exclude_account_ids"] = (
            capo_guardduty.types.detection_rule_account_ids.deserialize_json(
                data["excludeAccountIds"]
            )
        )
    return out
