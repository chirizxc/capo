"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#MessageAttributeName``."""

from typing import TypeAlias

"""Message attribute name. The ceiling is wide enough to hold a JSONata expression, because a name may be a literal or an expression resolved once per delivered event."""
MessageAttributeName: TypeAlias = str
