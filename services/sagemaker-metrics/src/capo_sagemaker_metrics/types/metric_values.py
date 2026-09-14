"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#MetricValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_metrics.types.double

MetricValues: TypeAlias = list["capo_sagemaker_metrics.types.double.Double"]


# --- restJson1 ser/de ---
def serialize_json(value: MetricValues) -> list:
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


def deserialize_json(data: list) -> MetricValues:
    return [float(item) for item in data if item is not None]
