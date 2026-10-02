"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AccessProfileType``."""

from typing import Literal, TypeAlias, cast

"""Who manages an access profile."""
AccessProfileType: TypeAlias = Literal[
    "SERVICE_MANAGED",
    "CUSTOMER_MANAGED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessProfileType) -> str:
    return value


def deserialize_cbor(data: str) -> AccessProfileType:
    return cast(AccessProfileType, data)
