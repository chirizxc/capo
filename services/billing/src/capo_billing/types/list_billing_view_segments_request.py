"""Generated from Smithy shape ``com.amazonaws.billing#ListBillingViewSegmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.billing_view_arn
    import capo_billing.types.billing_view_segment_time_range
    import capo_billing.types.billing_views_max_results
    import capo_billing.types.page_token


class ListBillingViewSegmentsRequest(TypedDict, closed=True):
    time_range: NotRequired[
        "capo_billing.types.billing_view_segment_time_range.BillingViewSegmentTimeRange"
    ]
    """<p> The billing period to query. If you don't provide a time range, the current billing period, which is the calendar month in UTC, is used. </p>"""
    arn: NotRequired["capo_billing.types.billing_view_arn.BillingViewArn"]
    """<p> The Amazon Resource Name (ARN) that uniquely identifies the billing view to query. If you don't provide an ARN, the caller's <code>PRIMARY</code> billing view is used. The ARN must reference a primary billing view. Custom billing views aren't supported. </p>"""
    max_results: NotRequired[
        "capo_billing.types.billing_views_max_results.BillingViewsMaxResults"
    ]
    """<p> The number of entries a paginated response contains. Valid values range from 1 to 100. The default is 100. </p>"""
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p> The pagination token that is used on subsequent calls to list billing view segments. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillingViewSegmentsRequest) -> dict:
    out: dict = {}
    if "time_range" in value:
        import capo_billing.types.billing_view_segment_time_range

        out["timeRange"] = (
            capo_billing.types.billing_view_segment_time_range.serialize_aws_json_1_0(
                value["time_range"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBillingViewSegmentsRequest:
    out: ListBillingViewSegmentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("timeRange") is not None:
        import capo_billing.types.billing_view_segment_time_range

        out["time_range"] = (
            capo_billing.types.billing_view_segment_time_range.deserialize_aws_json_1_0(
                data["timeRange"]
            )
        )
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
