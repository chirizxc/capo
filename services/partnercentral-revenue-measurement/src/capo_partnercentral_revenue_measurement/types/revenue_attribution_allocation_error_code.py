"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#RevenueAttributionAllocationErrorCode``."""

from typing import Literal, TypeAlias, cast

RevenueAttributionAllocationErrorCode: TypeAlias = Literal[
    "ALLOCATION_CAP_EXCEEDED",
    "RESOURCE_NOT_FOUND",
    "IMMUTABLE_ALLOCATION",
    "ACCESS_DENIED",
    "INVALID_VALUE",
    "CONCURRENT_MODIFICATION",
    "INTERNAL_ERROR",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevenueAttributionAllocationErrorCode) -> str:
    return value


def deserialize_cbor(data: str) -> RevenueAttributionAllocationErrorCode:
    return cast(RevenueAttributionAllocationErrorCode, data)
