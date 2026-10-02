"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#RevenueAttributionAllocationTaskStatus``."""

from typing import Literal, TypeAlias, cast

RevenueAttributionAllocationTaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevenueAttributionAllocationTaskStatus) -> str:
    return value


def deserialize_cbor(data: str) -> RevenueAttributionAllocationTaskStatus:
    return cast(RevenueAttributionAllocationTaskStatus, data)
