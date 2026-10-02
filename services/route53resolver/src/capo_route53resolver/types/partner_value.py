"""Generated from Smithy shape ``com.amazonaws.route53resolver#PartnerValue``."""

from typing import TypeAlias

"""<p>The identifier of a partner threat-protection product, returned in the <code>Value</code> field of a <a>FirewallRuleTypeDefinition</a> for the <code>PartnerThreatProtection</code> rule type. Pass this string as <code>PartnerThreatProtectionConfig.Partner</code> when creating a partner-managed firewall rule.</p>"""
PartnerValue: TypeAlias = str
