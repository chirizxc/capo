"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#RawMetricData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_metrics.types.double
    import capo_sagemaker_metrics.types.metric_name
    import capo_sagemaker_metrics.types.step
    import capo_sagemaker_metrics.types.timestamp


class RawMetricData(TypedDict, closed=True):
    metric_name: NotRequired["capo_sagemaker_metrics.types.metric_name.MetricName"]
    """<p>The name of the metric.</p>"""
    timestamp: NotRequired["capo_sagemaker_metrics.types.timestamp.Timestamp"]
    """<p>The time that the metric was recorded.</p>"""
    step: NotRequired["capo_sagemaker_metrics.types.step.Step"]
    """<p>The metric step (epoch). </p>"""
    value: NotRequired["capo_sagemaker_metrics.types.double.Double"]
    """<p>The metric value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RawMetricData) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "timestamp" in value:
        import capo_sagemaker_metrics.types.timestamp

        out["Timestamp"] = capo_sagemaker_metrics.types.timestamp.serialize_json(
            value["timestamp"]
        )
    if "step" in value:
        out["Step"] = value["step"]
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
    return out


def deserialize_json(data: dict) -> RawMetricData:
    out: RawMetricData = {}  # type: ignore[typeddict-item]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Timestamp") is not None:
        import capo_sagemaker_metrics.types.timestamp

        out["timestamp"] = capo_sagemaker_metrics.types.timestamp.deserialize_json(
            data["Timestamp"]
        )
    if data.get("Step") is not None:
        out["step"] = data["Step"]
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    return out
