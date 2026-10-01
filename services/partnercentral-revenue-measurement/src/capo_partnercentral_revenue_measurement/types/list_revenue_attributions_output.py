"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ListRevenueAttributionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.next_token
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_summaries


class ListRevenueAttributionsOutput(TypedDict, closed=True):
    revenue_attribution_summaries: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revenue_attribution_summaries.RevenueAttributionSummaries"
    ]
    """<p>The list of revenue attribution summaries.</p>"""
    next_token: NotRequired[
        "capo_partnercentral_revenue_measurement.types.next_token.NextToken"
    ]
    """<p>Token for pagination. Present if there are more results available.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRevenueAttributionsOutput) -> dict:
    out: dict = {}
    if "revenue_attribution_summaries" in value:
        import capo_partnercentral_revenue_measurement.types.revenue_attribution_summaries

        out["RevenueAttributionSummaries"] = (
            capo_partnercentral_revenue_measurement.types.revenue_attribution_summaries.serialize_cbor(
                value["revenue_attribution_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListRevenueAttributionsOutput:
    out: ListRevenueAttributionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("RevenueAttributionSummaries") is not None:
        import capo_partnercentral_revenue_measurement.types.revenue_attribution_summaries

        out["revenue_attribution_summaries"] = (
            capo_partnercentral_revenue_measurement.types.revenue_attribution_summaries.deserialize_cbor(
                data["RevenueAttributionSummaries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
