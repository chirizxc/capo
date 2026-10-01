"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AggregationThresholdType``."""

from typing import Literal, TypeAlias, cast

AggregationThresholdType: TypeAlias = Literal["COUNT_DISTINCT",]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationThresholdType) -> str:
    return value


def deserialize_json(data: str) -> AggregationThresholdType:
    return cast(AggregationThresholdType, data)
