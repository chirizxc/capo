"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#TagKey``."""

from typing import TypeAlias

"""Tag key. Must be non-empty; AWS-standard maximum length. Constraining the key (rather than a bare String) rejects empty-key payloads at the edge with a 400 ValidationException instead of faulting downstream as a 500."""
TagKey: TypeAlias = str
