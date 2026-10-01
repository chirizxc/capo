"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#RevenueAttributionAllocationSortField``."""

from typing import Literal, TypeAlias, cast

RevenueAttributionAllocationSortField: TypeAlias = Literal["EffectiveFrom",]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevenueAttributionAllocationSortField) -> str:
    return value


def deserialize_cbor(data: str) -> RevenueAttributionAllocationSortField:
    return cast(RevenueAttributionAllocationSortField, data)
