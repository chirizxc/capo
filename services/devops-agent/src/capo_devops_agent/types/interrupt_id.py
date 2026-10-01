"""Generated from Smithy shape ``com.amazonaws.devopsagent#InterruptId``."""

from typing import TypeAlias

"""<p>An opaque resume identifier issued by the service when an agent execution pauses for approval. The service emits this identifier in the streamed approval request; provide the same value on the resuming SendMessage so the service can resume the paused execution. The format is opaque — bounded for safe transit but intentionally not pattern-validated.</p>"""
InterruptId: TypeAlias = str
