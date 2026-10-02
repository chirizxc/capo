"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ClientToken``."""

from typing import TypeAlias

"""Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate."""
ClientToken: TypeAlias = str
