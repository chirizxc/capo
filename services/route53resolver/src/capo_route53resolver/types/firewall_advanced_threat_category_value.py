"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallAdvancedThreatCategoryValue``."""

from typing import TypeAlias

"""<p>The identifier of an Amazon Web Services-managed advanced threat category (for example, <code>PHISHING</code>), returned in the <code>Value</code> field of a <a>FirewallRuleTypeDefinition</a> for the <code>FirewallAdvancedThreatCategory</code> rule type. Pass this string as <code>FirewallAdvancedThreatCategoryConfig.Category</code> when creating a threat-category firewall rule.</p>"""
FirewallAdvancedThreatCategoryValue: TypeAlias = str
