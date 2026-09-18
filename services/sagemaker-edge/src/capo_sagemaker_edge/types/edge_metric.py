"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#EdgeMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_edge.types.dimension
    import capo_sagemaker_edge.types.metric
    import capo_sagemaker_edge.types.timestamp
    import capo_sagemaker_edge.types.value


class EdgeMetric(TypedDict, closed=True):
    dimension: NotRequired["capo_sagemaker_edge.types.dimension.Dimension"]
    """<p>The dimension of metrics published.</p>"""
    metric_name: NotRequired["capo_sagemaker_edge.types.metric.Metric"]
    """<p>Returns the name of the metric.</p>"""
    value: NotRequired["capo_sagemaker_edge.types.value.Value"]
    """<p>Returns the value of the metric.</p>"""
    timestamp: NotRequired["capo_sagemaker_edge.types.timestamp.Timestamp"]
    """<p>Timestamp of when the metric was requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EdgeMetric) -> dict:
    out: dict = {}
    if "dimension" in value:
        out["Dimension"] = value["dimension"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "value" in value:
        out["Value"] = (
            "NaN"
            if value["value"] != value["value"]
            else "Infinity"
            if value["value"] == float("inf")
            else "-Infinity"
            if value["value"] == float("-inf")
            else value["value"]
        )
    if "timestamp" in value:
        import capo_sagemaker_edge.types.timestamp

        out["Timestamp"] = capo_sagemaker_edge.types.timestamp.serialize_json(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> EdgeMetric:
    out: EdgeMetric = {}  # type: ignore[typeddict-item]
    if data.get("Dimension") is not None:
        out["dimension"] = data["Dimension"]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    if data.get("Timestamp") is not None:
        import capo_sagemaker_edge.types.timestamp

        out["timestamp"] = capo_sagemaker_edge.types.timestamp.deserialize_json(
            data["Timestamp"]
        )
    return out
