"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#EncryptionScope``."""

from typing import Literal, TypeAlias, cast

"""<p>Determines which newly created destination log groups are encrypted with the configured KMS key.</p>"""
EncryptionScope: TypeAlias = Literal[
    "ENCRYPTED_SOURCE_ONLY",
    "NEW_DESTINATION_LOG_GROUPS",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionScope) -> str:
    return value


def deserialize_json(data: str) -> EncryptionScope:
    return cast(EncryptionScope, data)
