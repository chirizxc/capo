"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ConditionalFieldBehavior``."""

from typing import TypeAlias

"""<p>The resolved requirement for a field when a conditional rule matches. Valid values are:</p> <p> <b>REQUIRED</b> — the field must be present; absence causes a validation error at submission time.</p> <p> <b>OPTIONAL</b> — the field may be present.</p> <p> <b>DISALLOWED</b> — the field must not be present; a submitted value is rejected with a validation error.</p>"""
ConditionalFieldBehavior: TypeAlias = str
