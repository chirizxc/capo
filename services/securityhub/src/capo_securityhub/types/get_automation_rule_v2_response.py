"""Generated from Smithy shape ``com.amazonaws.securityhub#GetAutomationRuleV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.automation_rules_action_list_v2
    import capo_securityhub.types.criteria
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.rule_order_value_v2
    import capo_securityhub.types.rule_status_v2
    import capo_securityhub.types.timestamp


class GetAutomationRuleV2Response(TypedDict, closed=True):
    rule_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the V2 automation rule.</p>"""
    rule_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the V2 automation rule.</p>"""
    rule_order: NotRequired[
        "capo_securityhub.types.rule_order_value_v2.RuleOrderValueV2"
    ]
    """<p>The value for the rule priority.</p>"""
    rule_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the V2 automation rule.</p>"""
    rule_status: NotRequired["capo_securityhub.types.rule_status_v2.RuleStatusV2"]
    """<p>The status of the V2 automation automation rule.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A description of the automation rule.</p>"""
    criteria: NotRequired["capo_securityhub.types.criteria.Criteria"]
    """<p>The filtering type and configuration of the V2 automation rule.</p>"""
    actions: NotRequired[
        "capo_securityhub.types.automation_rules_action_list_v2.AutomationRulesActionListV2"
    ]
    """<p>A list of actions performed when the rule criteria is met.</p>"""
    created_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>The timestamp when the V2 automation rule was created.</p>"""
    updated_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>The timestamp when the V2 automation rule was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomationRuleV2Response) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    if "rule_id" in value:
        out["RuleId"] = value["rule_id"]
    if "rule_order" in value:
        out["RuleOrder"] = (
            "NaN"
            if value["rule_order"] != value["rule_order"]
            else "Infinity"
            if value["rule_order"] == float("inf")
            else "-Infinity"
            if value["rule_order"] == float("-inf")
            else value["rule_order"]
        )
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "rule_status" in value:
        import capo_securityhub.types.rule_status_v2

        out["RuleStatus"] = capo_securityhub.types.rule_status_v2.serialize_json(
            value["rule_status"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "criteria" in value:
        import capo_securityhub.types.criteria

        out["Criteria"] = capo_securityhub.types.criteria.serialize_json(
            value["criteria"]
        )
    if "actions" in value:
        import capo_securityhub.types.automation_rules_action_list_v2

        out["Actions"] = (
            capo_securityhub.types.automation_rules_action_list_v2.serialize_json(
                value["actions"]
            )
        )
    if "created_at" in value:
        import capo_securityhub.types.timestamp

        out["CreatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityhub.types.timestamp

        out["UpdatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetAutomationRuleV2Response:
    out: GetAutomationRuleV2Response = {}  # type: ignore[typeddict-item]
    if data.get("RuleArn") is not None:
        out["rule_arn"] = data["RuleArn"]
    if data.get("RuleId") is not None:
        out["rule_id"] = data["RuleId"]
    if data.get("RuleOrder") is not None:
        out["rule_order"] = float(data["RuleOrder"])
    if data.get("RuleName") is not None:
        out["rule_name"] = data["RuleName"]
    if data.get("RuleStatus") is not None:
        import capo_securityhub.types.rule_status_v2

        out["rule_status"] = capo_securityhub.types.rule_status_v2.deserialize_json(
            data["RuleStatus"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Criteria") is not None:
        import capo_securityhub.types.criteria

        out["criteria"] = capo_securityhub.types.criteria.deserialize_json(
            data["Criteria"]
        )
    if data.get("Actions") is not None:
        import capo_securityhub.types.automation_rules_action_list_v2

        out["actions"] = (
            capo_securityhub.types.automation_rules_action_list_v2.deserialize_json(
                data["Actions"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_securityhub.types.timestamp

        out["created_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_securityhub.types.timestamp

        out["updated_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
