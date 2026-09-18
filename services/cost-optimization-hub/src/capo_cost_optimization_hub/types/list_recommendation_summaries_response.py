"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ListRecommendationSummariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.recommendation_summaries_list
    import capo_cost_optimization_hub.types.summary_metrics_result


class ListRecommendationSummariesResponse(TypedDict, closed=True):
    estimated_total_deduped_savings: NotRequired["float"]
    """<p>The total overall savings for the aggregated view.</p>"""
    items: NotRequired[
        "capo_cost_optimization_hub.types.recommendation_summaries_list.RecommendationSummariesList"
    ]
    """<p>A list of all savings recommendations.</p>"""
    group_by: NotRequired["str"]
    """<p>The dimension used to group the recommendations by.</p>"""
    currency_code: NotRequired["str"]
    """<p>The currency code used for the recommendation.</p>"""
    metrics: NotRequired[
        "capo_cost_optimization_hub.types.summary_metrics_result.SummaryMetricsResult"
    ]
    """<p>The results or descriptions for the additional metrics, based on whether the metrics were or were not requested.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to retrieve the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRecommendationSummariesResponse) -> dict:
    out: dict = {}
    if "estimated_total_deduped_savings" in value:
        out["estimatedTotalDedupedSavings"] = (
            "NaN"
            if value["estimated_total_deduped_savings"]
            != value["estimated_total_deduped_savings"]
            else "Infinity"
            if value["estimated_total_deduped_savings"] == float("inf")
            else "-Infinity"
            if value["estimated_total_deduped_savings"] == float("-inf")
            else value["estimated_total_deduped_savings"]
        )
    if "items" in value:
        import capo_cost_optimization_hub.types.recommendation_summaries_list

        out["items"] = (
            capo_cost_optimization_hub.types.recommendation_summaries_list.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "group_by" in value:
        out["groupBy"] = value["group_by"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "metrics" in value:
        import capo_cost_optimization_hub.types.summary_metrics_result

        out["metrics"] = (
            capo_cost_optimization_hub.types.summary_metrics_result.serialize_aws_json_1_0(
                value["metrics"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRecommendationSummariesResponse:
    out: ListRecommendationSummariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("estimatedTotalDedupedSavings") is not None:
        out["estimated_total_deduped_savings"] = float(
            data["estimatedTotalDedupedSavings"]
        )
    if data.get("items") is not None:
        import capo_cost_optimization_hub.types.recommendation_summaries_list

        out["items"] = (
            capo_cost_optimization_hub.types.recommendation_summaries_list.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if data.get("groupBy") is not None:
        out["group_by"] = data["groupBy"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("metrics") is not None:
        import capo_cost_optimization_hub.types.summary_metrics_result

        out["metrics"] = (
            capo_cost_optimization_hub.types.summary_metrics_result.deserialize_aws_json_1_0(
                data["metrics"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
