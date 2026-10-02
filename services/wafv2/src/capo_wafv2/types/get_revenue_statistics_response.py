"""Generated from Smithy shape ``com.amazonaws.wafv2#GetRevenueStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.next_marker
    import capo_wafv2.types.revenue_path_statistics_list
    import capo_wafv2.types.source_statistics_list


class GetRevenueStatisticsResponse(TypedDict, closed=True):
    source_statistics: NotRequired[
        "capo_wafv2.types.source_statistics_list.SourceStatisticsList"
    ]
    """<p>Statistics for top revenue sources (AI bots). Populated when <code>StatisticType</code> is <code>TOP_SOURCES_BY_REVENUE</code>.</p>"""
    revenue_path_statistics: NotRequired[
        "capo_wafv2.types.revenue_path_statistics_list.RevenuePathStatisticsList"
    ]
    """<p>Statistics for top revenue paths. Populated when <code>StatisticType</code> is <code>TOP_PATHS_BY_REVENUE</code>.</p>"""
    next_marker: NotRequired["capo_wafv2.types.next_marker.NextMarker"]
    """<p>When you get a paginated response, this marker indicates that additional results are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRevenueStatisticsResponse) -> dict:
    out: dict = {}
    if "source_statistics" in value:
        import capo_wafv2.types.source_statistics_list

        out["SourceStatistics"] = (
            capo_wafv2.types.source_statistics_list.serialize_aws_json_1_1(
                value["source_statistics"]
            )
        )
    if "revenue_path_statistics" in value:
        import capo_wafv2.types.revenue_path_statistics_list

        out["RevenuePathStatistics"] = (
            capo_wafv2.types.revenue_path_statistics_list.serialize_aws_json_1_1(
                value["revenue_path_statistics"]
            )
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRevenueStatisticsResponse:
    out: GetRevenueStatisticsResponse = {}  # type: ignore[typeddict-item]
    if data.get("SourceStatistics") is not None:
        import capo_wafv2.types.source_statistics_list

        out["source_statistics"] = (
            capo_wafv2.types.source_statistics_list.deserialize_aws_json_1_1(
                data["SourceStatistics"]
            )
        )
    if data.get("RevenuePathStatistics") is not None:
        import capo_wafv2.types.revenue_path_statistics_list

        out["revenue_path_statistics"] = (
            capo_wafv2.types.revenue_path_statistics_list.deserialize_aws_json_1_1(
                data["RevenuePathStatistics"]
            )
        )
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out
