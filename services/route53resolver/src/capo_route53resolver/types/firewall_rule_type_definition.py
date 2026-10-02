"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleTypeDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.display_name
    import capo_route53resolver.types.rule_type_description
    import capo_route53resolver.types.rule_type_name
    import capo_route53resolver.types.rule_type_value
    import capo_route53resolver.types.subscription_info


class FirewallRuleTypeDefinition(TypedDict, closed=True):
    rule_type: NotRequired["capo_route53resolver.types.rule_type_name.RuleTypeName"]
    """<p>The category or class of the rule type, such as <code>FirewallAdvancedContentCategory</code> or <code>FirewallAdvancedThreatCategory</code>.</p>"""
    value: NotRequired["capo_route53resolver.types.rule_type_value.RuleTypeValue"]
    """<p>The specific identifier within the rule type category, such as <code>VIOLENCE_AND_HATE_SPEECH</code> or <code>PHISHING</code>.</p>"""
    display_name: NotRequired["capo_route53resolver.types.display_name.DisplayName"]
    """<p>The display name of the rule type.</p>"""
    description: NotRequired[
        "capo_route53resolver.types.rule_type_description.RuleTypeDescription"
    ]
    """<p>A description of the rule type.</p>"""
    subscription_info: NotRequired[
        "capo_route53resolver.types.subscription_info.SubscriptionInfo"
    ]
    """<p>For rule types that require an external subscription (today, only the <code>PartnerThreatProtection</code> variant), describes the Amazon Web Services Marketplace product that backs the rule type. Absent for rule types that are managed by Amazon Web Services and do not require a separate subscription. See <a>SubscriptionInfo</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallRuleTypeDefinition) -> dict:
    out: dict = {}
    if "rule_type" in value:
        out["RuleType"] = value["rule_type"]
    if "value" in value:
        out["Value"] = value["value"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "subscription_info" in value:
        import capo_route53resolver.types.subscription_info

        out["SubscriptionInfo"] = (
            capo_route53resolver.types.subscription_info.serialize_aws_json_1_1(
                value["subscription_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallRuleTypeDefinition:
    out: FirewallRuleTypeDefinition = {}  # type: ignore[typeddict-item]
    if data.get("RuleType") is not None:
        out["rule_type"] = data["RuleType"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SubscriptionInfo") is not None:
        import capo_route53resolver.types.subscription_info

        out["subscription_info"] = (
            capo_route53resolver.types.subscription_info.deserialize_aws_json_1_1(
                data["SubscriptionInfo"]
            )
        )
    return out
