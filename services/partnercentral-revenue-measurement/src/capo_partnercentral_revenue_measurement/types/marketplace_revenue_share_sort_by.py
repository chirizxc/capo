"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#MarketplaceRevenueShareSortBy``."""

from typing import Literal, TypeAlias, cast

MarketplaceRevenueShareSortBy: TypeAlias = Literal["LastModifiedDate",]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MarketplaceRevenueShareSortBy) -> str:
    return value


def deserialize_cbor(data: str) -> MarketplaceRevenueShareSortBy:
    return cast(MarketplaceRevenueShareSortBy, data)
