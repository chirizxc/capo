"""Generated from Smithy shape ``com.amazonaws.wafv2#GetRevenueStatisticsSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.revenue_breakdown


class GetRevenueStatisticsSummaryResponse(TypedDict, closed=True):
    revenue_breakdown: NotRequired[
        "capo_wafv2.types.revenue_breakdown.RevenueBreakdown"
    ]
    """<p>The revenue breakdown summary for the specified time window and filters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRevenueStatisticsSummaryResponse) -> dict:
    out: dict = {}
    if "revenue_breakdown" in value:
        import capo_wafv2.types.revenue_breakdown

        out["RevenueBreakdown"] = (
            capo_wafv2.types.revenue_breakdown.serialize_aws_json_1_1(
                value["revenue_breakdown"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRevenueStatisticsSummaryResponse:
    out: GetRevenueStatisticsSummaryResponse = {}  # type: ignore[typeddict-item]
    if data.get("RevenueBreakdown") is not None:
        import capo_wafv2.types.revenue_breakdown

        out["revenue_breakdown"] = (
            capo_wafv2.types.revenue_breakdown.deserialize_aws_json_1_1(
                data["RevenueBreakdown"]
            )
        )
    return out
