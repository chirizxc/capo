"""Generated from Smithy shape ``com.amazonaws.connect#ChannelWorkloadBehaviorType``."""

from typing import Literal, TypeAlias, cast

ChannelWorkloadBehaviorType: TypeAlias = Literal[
    "ROUTE_CURRENT_CHANNEL_CURRENT_WORKLOADTYPE_ONLY",
    "ROUTE_CURRENT_CHANNEL_ANY_WORKLOADTYPE_ONLY",
    "ROUTE_ANY_CHANNEL_ANY_WORKLOAD_TYPE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelWorkloadBehaviorType) -> str:
    return value


def deserialize_json(data: str) -> ChannelWorkloadBehaviorType:
    return cast(ChannelWorkloadBehaviorType, data)
