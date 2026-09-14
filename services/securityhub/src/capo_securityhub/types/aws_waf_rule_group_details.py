"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRuleGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_waf_rule_group_rules_list
    import capo_securityhub.types.non_empty_string


class AwsWafRuleGroupDetails(TypedDict, closed=True):
    metric_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the metrics for this rule group. </p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the rule group. </p>"""
    rule_group_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the rule group. </p>"""
    rules: NotRequired[
        "capo_securityhub.types.aws_waf_rule_group_rules_list.AwsWafRuleGroupRulesList"
    ]
    """<p>Provides information about the rules attached to the rule group. These rules identify the web requests that you want to allow, block, or count. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRuleGroupDetails) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "rule_group_id" in value:
        out["RuleGroupId"] = value["rule_group_id"]
    if "rules" in value:
        import capo_securityhub.types.aws_waf_rule_group_rules_list

        out["Rules"] = (
            capo_securityhub.types.aws_waf_rule_group_rules_list.serialize_json(
                value["rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafRuleGroupDetails:
    out: AwsWafRuleGroupDetails = {}  # type: ignore[typeddict-item]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("RuleGroupId") is not None:
        out["rule_group_id"] = data["RuleGroupId"]
    if data.get("Rules") is not None:
        import capo_securityhub.types.aws_waf_rule_group_rules_list

        out["rules"] = (
            capo_securityhub.types.aws_waf_rule_group_rules_list.deserialize_json(
                data["Rules"]
            )
        )
    return out
