"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ServiceQuotaExceededExceptionReason``."""

from typing import Literal, TypeAlias, cast

ServiceQuotaExceededExceptionReason: TypeAlias = Literal[
    "ATTRIBUTION_LIMIT_EXCEEDED",
    "TAG_LIMIT_EXCEEDED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceQuotaExceededExceptionReason) -> str:
    return value


def deserialize_cbor(data: str) -> ServiceQuotaExceededExceptionReason:
    return cast(ServiceQuotaExceededExceptionReason, data)
