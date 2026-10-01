"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#MarketplaceRevenueShareAllocationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_summary

MarketplaceRevenueShareAllocationSummaryList: TypeAlias = list[
    "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_summary.MarketplaceRevenueShareAllocationSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MarketplaceRevenueShareAllocationSummaryList) -> list:
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_summary.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> MarketplaceRevenueShareAllocationSummaryList:
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_summary

    out: MarketplaceRevenueShareAllocationSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_summary.deserialize_cbor(
                item
            )
        )
    return out
