"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#FrameMetricValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.frame_metric_value

FrameMetricValues: TypeAlias = list[
    "capo_codeguruprofiler.types.frame_metric_value.FrameMetricValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: FrameMetricValues) -> list:
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


def deserialize_json(data: list) -> FrameMetricValues:
    return [float(item) for item in data if item is not None]
