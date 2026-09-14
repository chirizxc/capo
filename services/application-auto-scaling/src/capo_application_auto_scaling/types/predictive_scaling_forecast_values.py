"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#PredictiveScalingForecastValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.metric_scale

PredictiveScalingForecastValues: TypeAlias = list[
    "capo_application_auto_scaling.types.metric_scale.MetricScale"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictiveScalingForecastValues) -> list:
    return [
        (
            "NaN"
            if item != item
            else "Infinity"
            if item == float("inf")
            else "-Infinity"
            if item == float("-inf")
            else item
        )
        for item in value
    ]


def deserialize_aws_json_1_1(data: list) -> PredictiveScalingForecastValues:
    return [float(item) for item in data if item is not None]
