"""Generated from Smithy shape ``com.amazonaws.batch#CRAllocationStrategy``."""

from typing import Literal, TypeAlias, cast

CRAllocationStrategy: TypeAlias = Literal[
    "BEST_FIT",
    "BEST_FIT_PROGRESSIVE",
    "BEST_FIT_PROGRESSIVE_ORDERED",
    "SPOT_CAPACITY_OPTIMIZED",
    "SPOT_PRICE_CAPACITY_OPTIMIZED",
    "SPOT_CAPACITY_OPTIMIZED_PRIORITIZED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CRAllocationStrategy) -> str:
    return value


def deserialize_json(data: str) -> CRAllocationStrategy:
    return cast(CRAllocationStrategy, data)
