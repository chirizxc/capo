"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#MetricsByTime``."""

from typing_extensions import NotRequired, TypedDict


class MetricsByTime(TypedDict, closed=True):
    score: NotRequired["float"]
    """<p>The efficiency score for this time period. The score represents a measure of how effectively the cloud resources are being optimized, with higher scores indicating better optimization performance.</p>"""
    savings: NotRequired["float"]
    """<p>The estimated savings amount for this time period, representing the potential cost reduction achieved through optimization recommendations.</p>"""
    spend: NotRequired["float"]
    """<p>The total spending amount for this time period.</p>"""
    timestamp: NotRequired["str"]
    """<p>The timestamp for this data point. The format depends on the granularity: YYYY-MM-DD for daily metrics, or YYYY-MM for monthly metrics.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricsByTime) -> dict:
    out: dict = {}
    if "score" in value:
        out["score"] = (
            "NaN"
            if value["score"] != value["score"]
            else "Infinity"
            if value["score"] == float("inf")
            else "-Infinity"
            if value["score"] == float("-inf")
            else value["score"]
        )
    if "savings" in value:
        out["savings"] = (
            "NaN"
            if value["savings"] != value["savings"]
            else "Infinity"
            if value["savings"] == float("inf")
            else "-Infinity"
            if value["savings"] == float("-inf")
            else value["savings"]
        )
    if "spend" in value:
        out["spend"] = (
            "NaN"
            if value["spend"] != value["spend"]
            else "Infinity"
            if value["spend"] == float("inf")
            else "-Infinity"
            if value["spend"] == float("-inf")
            else value["spend"]
        )
    if "timestamp" in value:
        out["timestamp"] = value["timestamp"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MetricsByTime:
    out: MetricsByTime = {}  # type: ignore[typeddict-item]
    if data.get("score") is not None:
        out["score"] = float(data["score"])
    if data.get("savings") is not None:
        out["savings"] = float(data["savings"])
    if data.get("spend") is not None:
        out["spend"] = float(data["spend"])
    if data.get("timestamp") is not None:
        out["timestamp"] = data["timestamp"]
    return out
