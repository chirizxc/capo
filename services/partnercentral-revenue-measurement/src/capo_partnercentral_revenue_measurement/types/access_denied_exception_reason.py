"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#AccessDeniedExceptionReason``."""

from typing import Literal, TypeAlias, cast

AccessDeniedExceptionReason: TypeAlias = Literal["ACCESS_DENIED",]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessDeniedExceptionReason) -> str:
    return value


def deserialize_cbor(data: str) -> AccessDeniedExceptionReason:
    return cast(AccessDeniedExceptionReason, data)
