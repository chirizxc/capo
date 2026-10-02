"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "REQUEST_VALIDATION_FAILED",
    "BUSINESS_VALIDATION_FAILED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ValidationExceptionReason) -> str:
    return value


def deserialize_cbor(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
