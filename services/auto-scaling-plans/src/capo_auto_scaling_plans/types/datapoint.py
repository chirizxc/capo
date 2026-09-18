"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#Datapoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.metric_scale
    import capo_auto_scaling_plans.types.timestamp_type


class Datapoint(TypedDict, closed=True):
    timestamp: NotRequired["capo_auto_scaling_plans.types.timestamp_type.TimestampType"]
    """<p>The time stamp for the data point in UTC format.</p>"""
    value: NotRequired["capo_auto_scaling_plans.types.metric_scale.MetricScale"]
    """<p>The value of the data point.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Datapoint) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import capo_auto_scaling_plans.types.timestamp_type

        out["Timestamp"] = (
            capo_auto_scaling_plans.types.timestamp_type.serialize_aws_json_1_1(
                value["timestamp"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> Datapoint:
    out: Datapoint = {}  # type: ignore[typeddict-item]
    if data.get("Timestamp") is not None:
        import capo_auto_scaling_plans.types.timestamp_type

        out["timestamp"] = (
            capo_auto_scaling_plans.types.timestamp_type.deserialize_aws_json_1_1(
                data["Timestamp"]
            )
        )
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    return out
