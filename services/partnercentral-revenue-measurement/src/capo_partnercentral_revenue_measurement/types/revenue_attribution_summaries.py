"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#RevenueAttributionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.attribution_summary

RevenueAttributionSummaries: TypeAlias = list[
    "capo_partnercentral_revenue_measurement.types.attribution_summary.AttributionSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevenueAttributionSummaries) -> list:
    import capo_partnercentral_revenue_measurement.types.attribution_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_revenue_measurement.types.attribution_summary.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> RevenueAttributionSummaries:
    import capo_partnercentral_revenue_measurement.types.attribution_summary

    out: RevenueAttributionSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_revenue_measurement.types.attribution_summary.deserialize_cbor(
                item
            )
        )
    return out
