"""Generated from Smithy shape ``com.amazonaws.sts#minimumSessionTokenSizeType``."""

from typing import TypeAlias

"""The minimum size, in bytes, of the session token that STS issues for the request. STS increases the session token to at least this size, regardless of its actual content. The value must not exceed 4,096 bytes. When set to 0 or not specified, the session token size is unchanged."""
minimumSessionTokenSizeType: TypeAlias = int
