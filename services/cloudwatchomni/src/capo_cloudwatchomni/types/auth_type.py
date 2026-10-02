"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AuthType``."""

from typing import Literal, TypeAlias, cast

"""The authentication method that an integration uses to connect to its external system."""
AuthType: TypeAlias = Literal[
    "NONE",
    "OAUTH2",
    "API_KEY",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AuthType) -> str:
    return value


def deserialize_cbor(data: str) -> AuthType:
    return cast(AuthType, data)
