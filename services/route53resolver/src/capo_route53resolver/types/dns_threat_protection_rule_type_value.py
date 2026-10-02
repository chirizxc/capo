"""Generated from Smithy shape ``com.amazonaws.route53resolver#DnsThreatProtectionRuleTypeValue``."""

from typing import TypeAlias

"""<p>The identifier of a built-in DNS Firewall Advanced threat detector. Known values are <code>DGA</code>, <code>DNS_TUNNELING</code>, and <code>DICTIONARY_DGA</code>. Returned in the <code>Value</code> field of a <a>FirewallRuleTypeDefinition</a> for the <code>DnsThreatProtection</code> rule type, and used as <code>DnsThreatProtectionRuleTypeConfig.Value</code> when creating a DNS threat protection firewall rule.</p>"""
DnsThreatProtectionRuleTypeValue: TypeAlias = str
