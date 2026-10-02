"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#RevenueAttributionAllocationAction``."""

from typing import Literal, TypeAlias, cast

RevenueAttributionAllocationAction: TypeAlias = Literal[
    "CREATE",
    "UPDATE",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevenueAttributionAllocationAction) -> str:
    return value


def deserialize_cbor(data: str) -> RevenueAttributionAllocationAction:
    return cast(RevenueAttributionAllocationAction, data)
