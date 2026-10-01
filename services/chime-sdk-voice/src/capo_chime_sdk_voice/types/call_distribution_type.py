"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CallDistributionType``."""

from typing import Literal, TypeAlias, cast

CallDistributionType: TypeAlias = Literal[
    "PriorityWeightedDistribution",
    "LoadBalancedDistribution",
]


# --- restJson1 ser/de ---
def serialize_json(value: CallDistributionType) -> str:
    return value


def deserialize_json(data: str) -> CallDistributionType:
    return cast(CallDistributionType, data)
