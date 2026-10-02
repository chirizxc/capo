"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleStatus``."""

from typing import TypeAlias

"""<p>The lifecycle state of a DNS Firewall rule. Known values:</p> <ul> <li> <p> <code>CREATING</code> — DNS Firewall is provisioning the rule. Rules created with the <code>PartnerThreatProtection</code> rule type begin in this state while DNS Firewall verifies the calling account's Amazon Web Services Marketplace entitlement.</p> </li> <li> <p> <code>COMPLETE</code> — The rule is provisioned and enforcing matches.</p> </li> <li> <p> <code>CREATION_FAILED</code> — Provisioning failed. <a>UpdateFirewallRule</a> rejects updates to a rule in this state; the rule must be removed with <a>DeleteFirewallRule</a>.</p> </li> </ul>"""
FirewallRuleStatus: TypeAlias = str
