"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DeepLinkCode``."""

from typing import TypeAlias

"""A one-time deep-link code exchanged for a domain-scoped session. Sensitive: it can be redeemed for a session token, so it is redacted from request logs and CloudTrail."""
DeepLinkCode: TypeAlias = str
