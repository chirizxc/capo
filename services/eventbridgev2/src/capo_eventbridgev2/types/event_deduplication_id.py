"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#EventDeduplicationId``."""

from typing import TypeAlias

"""Customer-supplied deduplication token for a published event. The token must contain at least one non-whitespace character. Values are treated literally, including text resembling a JSONata expression."""
EventDeduplicationId: TypeAlias = str
