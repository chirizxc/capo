"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#MarketplaceRevenueShareSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_summary

MarketplaceRevenueShareSummaryList: TypeAlias = list[
    "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_summary.MarketplaceRevenueShareSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MarketplaceRevenueShareSummaryList) -> list:
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_summary.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> MarketplaceRevenueShareSummaryList:
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_summary

    out: MarketplaceRevenueShareSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_summary.deserialize_cbor(
                item
            )
        )
    return out
