"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#MarketplaceRevenueShareAllocationSortField``."""

from typing import Literal, TypeAlias, cast

MarketplaceRevenueShareAllocationSortField: TypeAlias = Literal["EffectiveFrom",]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MarketplaceRevenueShareAllocationSortField) -> str:
    return value


def deserialize_cbor(data: str) -> MarketplaceRevenueShareAllocationSortField:
    return cast(MarketplaceRevenueShareAllocationSortField, data)
