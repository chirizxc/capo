"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ConditionOperator``."""

from typing import TypeAlias

"""<p>The operator used to compare a dependency field's value in a <b>FieldCondition</b>. Valid values are <b>EQUALS</b>, <b>NOT_EQUALS</b>, <b>IN</b>, <b>NOT_IN</b>, <b>HAS_VALUE</b>, and <b>NO_VALUE</b>. Unknown operators evaluate to false, which causes the containing rule to be skipped.</p>"""
ConditionOperator: TypeAlias = str
