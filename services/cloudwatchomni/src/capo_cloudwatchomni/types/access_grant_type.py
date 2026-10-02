"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AccessGrantType``."""

from typing import Literal, TypeAlias, cast

"""Who manages an access grant."""
AccessGrantType: TypeAlias = Literal[
    "SERVICE_MANAGED",
    "CUSTOMER_MANAGED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessGrantType) -> str:
    return value


def deserialize_cbor(data: str) -> AccessGrantType:
    return cast(AccessGrantType, data)
