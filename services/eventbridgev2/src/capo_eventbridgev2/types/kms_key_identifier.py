"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#KmsKeyIdentifier``."""

from typing import TypeAlias

"""Identifier of the AWS KMS customer managed key used to encrypt events: a key ID, key ARN, alias name, or alias ARN. When absent, events are encrypted with an AWS owned key."""
KmsKeyIdentifier: TypeAlias = str
