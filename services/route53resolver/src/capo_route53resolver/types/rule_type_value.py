"""Generated from Smithy shape ``com.amazonaws.route53resolver#RuleTypeValue``."""

from typing import TypeAlias

"""<p>The variant-specific value of a rule type, returned in the <code>Value</code> field of a <a>FirewallRuleTypeDefinition</a>. The interpretation of this string depends on <code>RuleType</code>; see <a>FirewallAdvancedContentCategoryValue</a>, <a>FirewallAdvancedThreatCategoryValue</a>, <a>DnsThreatProtectionRuleTypeValue</a>, or <a>PartnerValue</a>.</p>"""
RuleTypeValue: TypeAlias = str
