"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AggregationThresholdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.aggregation_threshold

AggregationThresholdList: TypeAlias = list[
    "capo_cleanrooms.types.aggregation_threshold.AggregationThreshold"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationThresholdList) -> list:
    import capo_cleanrooms.types.aggregation_threshold

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.aggregation_threshold.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregationThresholdList:
    import capo_cleanrooms.types.aggregation_threshold

    out: AggregationThresholdList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cleanrooms.types.aggregation_threshold.deserialize_json(item))
    return out
