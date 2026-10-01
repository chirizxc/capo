"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#MarketplaceProductIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.marketplace_product_id

MarketplaceProductIdList: TypeAlias = list[
    "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MarketplaceProductIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> MarketplaceProductIdList:
    return [item for item in data if item is not None]
