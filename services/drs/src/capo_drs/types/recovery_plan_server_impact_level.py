"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanServerImpactLevel``."""

from typing import TypeAlias

"""<p>The impact level of a server within a Recovery Plan step. <code>CRITICAL</code> means the step fails if this server fails. <code>OPTIONAL</code> means the step continues even if this server fails.</p>"""
RecoveryPlanServerImpactLevel: TypeAlias = str
