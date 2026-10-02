"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#MarketplaceRevenueShareTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.tag

MarketplaceRevenueShareTagList: TypeAlias = list[
    "capo_partnercentral_revenue_measurement.types.tag.Tag"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MarketplaceRevenueShareTagList) -> list:
    import capo_partnercentral_revenue_measurement.types.tag

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_revenue_measurement.types.tag.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> MarketplaceRevenueShareTagList:
    import capo_partnercentral_revenue_measurement.types.tag

    out: MarketplaceRevenueShareTagList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_revenue_measurement.types.tag.deserialize_cbor(item)
        )
    return out
