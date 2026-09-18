"""Generated from Smithy shape ``com.amazonaws.xray#ServiceStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.error_statistics
    import capo_xray.types.fault_statistics
    import capo_xray.types.nullable_double
    import capo_xray.types.nullable_long


class ServiceStatistics(TypedDict, closed=True):
    ok_count: NotRequired["capo_xray.types.nullable_long.NullableLong"]
    """<p>The number of requests that completed with a 2xx Success status code.</p>"""
    error_statistics: NotRequired["capo_xray.types.error_statistics.ErrorStatistics"]
    """<p>Information about requests that failed with a 4xx Client Error status code.</p>"""
    fault_statistics: NotRequired["capo_xray.types.fault_statistics.FaultStatistics"]
    """<p>Information about requests that failed with a 5xx Server Error status code.</p>"""
    total_count: NotRequired["capo_xray.types.nullable_long.NullableLong"]
    """<p>The total number of completed requests.</p>"""
    total_response_time: NotRequired["capo_xray.types.nullable_double.NullableDouble"]
    """<p>The aggregate response time of completed requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceStatistics) -> dict:
    out: dict = {}
    if "ok_count" in value:
        out["OkCount"] = value["ok_count"]
    if "error_statistics" in value:
        import capo_xray.types.error_statistics

        out["ErrorStatistics"] = capo_xray.types.error_statistics.serialize_json(
            value["error_statistics"]
        )
    if "fault_statistics" in value:
        import capo_xray.types.fault_statistics

        out["FaultStatistics"] = capo_xray.types.fault_statistics.serialize_json(
            value["fault_statistics"]
        )
    if "total_count" in value:
        out["TotalCount"] = value["total_count"]
    if "total_response_time" in value:
        out["TotalResponseTime"] = (
            "NaN"
            if value["total_response_time"] != value["total_response_time"]
            else "Infinity"
            if value["total_response_time"] == float("inf")
            else "-Infinity"
            if value["total_response_time"] == float("-inf")
            else value["total_response_time"]
        )
    return out


def deserialize_json(data: dict) -> ServiceStatistics:
    out: ServiceStatistics = {}  # type: ignore[typeddict-item]
    if data.get("OkCount") is not None:
        out["ok_count"] = data["OkCount"]
    if data.get("ErrorStatistics") is not None:
        import capo_xray.types.error_statistics

        out["error_statistics"] = capo_xray.types.error_statistics.deserialize_json(
            data["ErrorStatistics"]
        )
    if data.get("FaultStatistics") is not None:
        import capo_xray.types.fault_statistics

        out["fault_statistics"] = capo_xray.types.fault_statistics.deserialize_json(
            data["FaultStatistics"]
        )
    if data.get("TotalCount") is not None:
        out["total_count"] = data["TotalCount"]
    if data.get("TotalResponseTime") is not None:
        out["total_response_time"] = float(data["TotalResponseTime"])
    return out
