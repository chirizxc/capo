"""Generated from Smithy shape ``com.amazonaws.signin#ClientId``."""

from typing import TypeAlias

"""Client identifier pattern for AWS Sign-In devtools clients The ARN used by client as part of Sign-In onboarding. Expected values: - arn:aws:signin:::devtools/cross-device (for cross-device devtools login) - arn:aws:signin:::devtools/same-device (for same-device devtools login)"""
ClientId: TypeAlias = str
