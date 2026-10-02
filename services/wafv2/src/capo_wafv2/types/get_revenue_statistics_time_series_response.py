"""Generated from Smithy shape ``com.amazonaws.wafv2#GetRevenueStatisticsTimeSeriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.data_points_list
    import capo_wafv2.types.next_marker


class GetRevenueStatisticsTimeSeriesResponse(TypedDict, closed=True):
    data_points: NotRequired["capo_wafv2.types.data_points_list.DataPointsList"]
    """<p>The list of time series data points.</p>"""
    next_marker: NotRequired["capo_wafv2.types.next_marker.NextMarker"]
    """<p>When you get a paginated response, this marker indicates that additional results are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRevenueStatisticsTimeSeriesResponse) -> dict:
    out: dict = {}
    if "data_points" in value:
        import capo_wafv2.types.data_points_list

        out["DataPoints"] = capo_wafv2.types.data_points_list.serialize_aws_json_1_1(
            value["data_points"]
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRevenueStatisticsTimeSeriesResponse:
    out: GetRevenueStatisticsTimeSeriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("DataPoints") is not None:
        import capo_wafv2.types.data_points_list

        out["data_points"] = capo_wafv2.types.data_points_list.deserialize_aws_json_1_1(
            data["DataPoints"]
        )
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out
