"""Generated from Smithy shape ``com.amazonaws.batch#CRUpdateAllocationStrategy``."""

from typing import Literal, TypeAlias, cast

CRUpdateAllocationStrategy: TypeAlias = Literal[
    "BEST_FIT_PROGRESSIVE",
    "BEST_FIT_PROGRESSIVE_ORDERED",
    "SPOT_CAPACITY_OPTIMIZED",
    "SPOT_PRICE_CAPACITY_OPTIMIZED",
    "SPOT_CAPACITY_OPTIMIZED_PRIORITIZED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CRUpdateAllocationStrategy) -> str:
    return value


def deserialize_json(data: str) -> CRUpdateAllocationStrategy:
    return cast(CRUpdateAllocationStrategy, data)
