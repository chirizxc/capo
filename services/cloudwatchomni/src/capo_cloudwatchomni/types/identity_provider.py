"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#IdentityProvider``."""

from typing import Literal, TypeAlias, cast

"""Identity provider type for a domain. Determines which identity mechanisms are active for authentication."""
IdentityProvider: TypeAlias = Literal[
    "IAM",
    "IDC",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdentityProvider) -> str:
    return value


def deserialize_cbor(data: str) -> IdentityProvider:
    return cast(IdentityProvider, data)
