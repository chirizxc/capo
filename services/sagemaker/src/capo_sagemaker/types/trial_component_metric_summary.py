"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentMetricSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.metric_name
    import capo_sagemaker.types.optional_double
    import capo_sagemaker.types.optional_integer
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.trial_component_source_arn


class TrialComponentMetricSummary(TypedDict, closed=True):
    metric_name: NotRequired["capo_sagemaker.types.metric_name.MetricName"]
    """<p>The name of the metric.</p>"""
    source_arn: NotRequired[
        "capo_sagemaker.types.trial_component_source_arn.TrialComponentSourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the source.</p>"""
    time_stamp: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the metric was last updated.</p>"""
    max: NotRequired["capo_sagemaker.types.optional_double.OptionalDouble"]
    """<p>The maximum value of the metric.</p>"""
    min: NotRequired["capo_sagemaker.types.optional_double.OptionalDouble"]
    """<p>The minimum value of the metric.</p>"""
    last: NotRequired["capo_sagemaker.types.optional_double.OptionalDouble"]
    """<p>The most recent value of the metric.</p>"""
    count: NotRequired["capo_sagemaker.types.optional_integer.OptionalInteger"]
    """<p>The number of samples used to generate the metric.</p>"""
    avg: NotRequired["capo_sagemaker.types.optional_double.OptionalDouble"]
    """<p>The average value of the metric.</p>"""
    std_dev: NotRequired["capo_sagemaker.types.optional_double.OptionalDouble"]
    """<p>The standard deviation of the metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialComponentMetricSummary) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "time_stamp" in value:
        import capo_sagemaker.types.timestamp

        out["TimeStamp"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["time_stamp"]
        )
    if "max" in value:
        out["Max"] = (
            "NaN"
            if value["max"] != value["max"]
            else "Infinity"
            if value["max"] == float("inf")
            else "-Infinity"
            if value["max"] == float("-inf")
            else value["max"]
        )
    if "min" in value:
        out["Min"] = (
            "NaN"
            if value["min"] != value["min"]
            else "Infinity"
            if value["min"] == float("inf")
            else "-Infinity"
            if value["min"] == float("-inf")
            else value["min"]
        )
    if "last" in value:
        out["Last"] = (
            "NaN"
            if value["last"] != value["last"]
            else "Infinity"
            if value["last"] == float("inf")
            else "-Infinity"
            if value["last"] == float("-inf")
            else value["last"]
        )
    if "count" in value:
        out["Count"] = value["count"]
    if "avg" in value:
        out["Avg"] = (
            "NaN"
            if value["avg"] != value["avg"]
            else "Infinity"
            if value["avg"] == float("inf")
            else "-Infinity"
            if value["avg"] == float("-inf")
            else value["avg"]
        )
    if "std_dev" in value:
        out["StdDev"] = (
            "NaN"
            if value["std_dev"] != value["std_dev"]
            else "Infinity"
            if value["std_dev"] == float("inf")
            else "-Infinity"
            if value["std_dev"] == float("-inf")
            else value["std_dev"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrialComponentMetricSummary:
    out: TrialComponentMetricSummary = {}  # type: ignore[typeddict-item]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("SourceArn") is not None:
        out["source_arn"] = data["SourceArn"]
    if data.get("TimeStamp") is not None:
        import capo_sagemaker.types.timestamp

        out["time_stamp"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["TimeStamp"]
        )
    if data.get("Max") is not None:
        out["max"] = float(data["Max"])
    if data.get("Min") is not None:
        out["min"] = float(data["Min"])
    if data.get("Last") is not None:
        out["last"] = float(data["Last"])
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    if data.get("Avg") is not None:
        out["avg"] = float(data["Avg"])
    if data.get("StdDev") is not None:
        out["std_dev"] = float(data["StdDev"])
    return out
