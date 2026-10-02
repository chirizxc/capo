"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.dns_threat_protection_rule_type_config
    import capo_route53resolver.types.firewall_advanced_content_category_config
    import capo_route53resolver.types.firewall_advanced_threat_category_config
    import capo_route53resolver.types.partner_threat_protection_config


class FirewallRuleType(TypedDict, closed=True):
    partner_threat_protection: NotRequired[
        "capo_route53resolver.types.partner_threat_protection_config.PartnerThreatProtectionConfig"
    ]
    """<p>Configures the rule to match a third-party threat feed delivered through Amazon Web Services Marketplace. The calling account must hold an active subscription to the partner product named in <code>Partner</code>; if the subscription is missing or revoked, the rule is created with <code>Status</code> <code>CREATION_FAILED</code> and cannot be modified — only deleted. See <a>PartnerThreatProtectionConfig</a>.</p>"""
    firewall_advanced_content_category: NotRequired[
        "capo_route53resolver.types.firewall_advanced_content_category_config.FirewallAdvancedContentCategoryConfig"
    ]
    """<p>Configures the rule to match an Amazon Web Services-managed content category (for example, <code>VIOLENCE_AND_HATE_SPEECH</code>). See <a>FirewallAdvancedContentCategoryConfig</a>.</p>"""
    firewall_advanced_threat_category: NotRequired[
        "capo_route53resolver.types.firewall_advanced_threat_category_config.FirewallAdvancedThreatCategoryConfig"
    ]
    """<p>Configures the rule to match an Amazon Web Services-managed advanced threat category (for example, <code>PHISHING</code>). See <a>FirewallAdvancedThreatCategoryConfig</a>.</p>"""
    dns_threat_protection: NotRequired[
        "capo_route53resolver.types.dns_threat_protection_rule_type_config.DnsThreatProtectionRuleTypeConfig"
    ]
    """<p>Configures the rule to match a built-in DNS Firewall Advanced threat detector — <code>DGA</code>, <code>DNS_TUNNELING</code>, or <code>DICTIONARY_DGA</code>. See <a>DnsThreatProtectionRuleTypeConfig</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallRuleType) -> dict:
    out: dict = {}
    if "partner_threat_protection" in value:
        import capo_route53resolver.types.partner_threat_protection_config

        out["PartnerThreatProtection"] = (
            capo_route53resolver.types.partner_threat_protection_config.serialize_aws_json_1_1(
                value["partner_threat_protection"]
            )
        )
    if "firewall_advanced_content_category" in value:
        import capo_route53resolver.types.firewall_advanced_content_category_config

        out["FirewallAdvancedContentCategory"] = (
            capo_route53resolver.types.firewall_advanced_content_category_config.serialize_aws_json_1_1(
                value["firewall_advanced_content_category"]
            )
        )
    if "firewall_advanced_threat_category" in value:
        import capo_route53resolver.types.firewall_advanced_threat_category_config

        out["FirewallAdvancedThreatCategory"] = (
            capo_route53resolver.types.firewall_advanced_threat_category_config.serialize_aws_json_1_1(
                value["firewall_advanced_threat_category"]
            )
        )
    if "dns_threat_protection" in value:
        import capo_route53resolver.types.dns_threat_protection_rule_type_config

        out["DnsThreatProtection"] = (
            capo_route53resolver.types.dns_threat_protection_rule_type_config.serialize_aws_json_1_1(
                value["dns_threat_protection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallRuleType:
    out: FirewallRuleType = {}  # type: ignore[typeddict-item]
    if data.get("PartnerThreatProtection") is not None:
        import capo_route53resolver.types.partner_threat_protection_config

        out["partner_threat_protection"] = (
            capo_route53resolver.types.partner_threat_protection_config.deserialize_aws_json_1_1(
                data["PartnerThreatProtection"]
            )
        )
    if data.get("FirewallAdvancedContentCategory") is not None:
        import capo_route53resolver.types.firewall_advanced_content_category_config

        out["firewall_advanced_content_category"] = (
            capo_route53resolver.types.firewall_advanced_content_category_config.deserialize_aws_json_1_1(
                data["FirewallAdvancedContentCategory"]
            )
        )
    if data.get("FirewallAdvancedThreatCategory") is not None:
        import capo_route53resolver.types.firewall_advanced_threat_category_config

        out["firewall_advanced_threat_category"] = (
            capo_route53resolver.types.firewall_advanced_threat_category_config.deserialize_aws_json_1_1(
                data["FirewallAdvancedThreatCategory"]
            )
        )
    if data.get("DnsThreatProtection") is not None:
        import capo_route53resolver.types.dns_threat_protection_rule_type_config

        out["dns_threat_protection"] = (
            capo_route53resolver.types.dns_threat_protection_rule_type_config.deserialize_aws_json_1_1(
                data["DnsThreatProtection"]
            )
        )
    return out
