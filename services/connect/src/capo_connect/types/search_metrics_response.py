"""Generated from Smithy shape ``com.amazonaws.connect#SearchMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.approximate_total_count
    import capo_connect.types.metric_search_summary_list
    import capo_connect.types.next_token


class SearchMetricsResponse(TypedDict, closed=True):
    metrics: NotRequired[
        "capo_connect.types.metric_search_summary_list.MetricSearchSummaryList"
    ]
    """<p>The metrics that matched the search criteria.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "capo_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The approximate total number of metrics that matched your search criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchMetricsResponse) -> dict:
    out: dict = {}
    if "metrics" in value:
        import capo_connect.types.metric_search_summary_list

        out["Metrics"] = capo_connect.types.metric_search_summary_list.serialize_json(
            value["metrics"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchMetricsResponse:
    out: SearchMetricsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Metrics") is not None:
        import capo_connect.types.metric_search_summary_list

        out["metrics"] = capo_connect.types.metric_search_summary_list.deserialize_json(
            data["Metrics"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ApproximateTotalCount") is not None:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
