"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallAdvancedContentCategoryValue``."""

from typing import TypeAlias

"""<p>The identifier of an Amazon Web Services-managed content category (for example, <code>VIOLENCE_AND_HATE_SPEECH</code>), returned in the <code>Value</code> field of a <a>FirewallRuleTypeDefinition</a> for the <code>FirewallAdvancedContentCategory</code> rule type. Pass this string as <code>FirewallAdvancedContentCategoryConfig.Category</code> when creating a content-category firewall rule.</p>"""
FirewallAdvancedContentCategoryValue: TypeAlias = str
