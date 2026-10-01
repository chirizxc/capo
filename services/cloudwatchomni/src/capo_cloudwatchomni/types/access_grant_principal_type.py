"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AccessGrantPrincipalType``."""

from typing import Literal, TypeAlias, cast

"""Type of principal receiving the grant."""
AccessGrantPrincipalType: TypeAlias = Literal[
    "IDC_USER",
    "IDC_GROUP",
    "IAM_USER",
    "IAM_ROLE",
    "IAM_ROOT",
    "ACCESS_PROFILE",
    "ALERT",
    "AGENT",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessGrantPrincipalType) -> str:
    return value


def deserialize_cbor(data: str) -> AccessGrantPrincipalType:
    return cast(AccessGrantPrincipalType, data)
