"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateCustomDetectionRuleOrgConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.association_mode
    import capo_guardduty.types.client_token
    import capo_guardduty.types.detection_rule_account_ids
    import capo_guardduty.types.rule_id


class CreateCustomDetectionRuleOrgConfigurationRequest(TypedDict, closed=True):
    rule_id: NotRequired["capo_guardduty.types.rule_id.RuleId"]
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
    client_token: NotRequired["capo_guardduty.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomDetectionRuleOrgConfigurationRequest) -> dict:
    out: dict = {}
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateCustomDetectionRuleOrgConfigurationRequest:
    out: CreateCustomDetectionRuleOrgConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
