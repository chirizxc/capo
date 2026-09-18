"""Generated from Smithy shape ``com.amazonaws.iot#AdditionalMetricsToRetainList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.behavior_metric

AdditionalMetricsToRetainList: TypeAlias = list[
    "capo_iot.types.behavior_metric.BehaviorMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalMetricsToRetainList) -> list:
    return list(value)


def deserialize_json(data: list) -> AdditionalMetricsToRetainList:
    return [item for item in data if item is not None]
