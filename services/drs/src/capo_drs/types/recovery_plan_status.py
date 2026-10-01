"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanStatus``."""

from typing import TypeAlias

"""<p>Recovery Plan status. <code>ACTIVE</code> means executable. <code>INVALID</code> means the plan has no <code>SERVER</code> type steps and cannot be executed.</p>"""
RecoveryPlanStatus: TypeAlias = str
