"""Generated from Smithy shape ``com.amazonaws.quicksight#CredentialStatus``."""

from typing import Literal, TypeAlias, cast

CredentialStatus: TypeAlias = Literal[
    "CONNECTED",
    "AUTH_FAILED",
    "NOT_VERIFIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CredentialStatus) -> str:
    return value


def deserialize_json(data: str) -> CredentialStatus:
    return cast(CredentialStatus, data)
