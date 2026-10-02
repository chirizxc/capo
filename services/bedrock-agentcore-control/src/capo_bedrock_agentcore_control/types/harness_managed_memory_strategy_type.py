"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessManagedMemoryStrategyType``."""

from typing import Literal, TypeAlias, cast

HarnessManagedMemoryStrategyType: TypeAlias = Literal[
    "SEMANTIC",
    "SUMMARIZATION",
    "USER_PREFERENCE",
    "EPISODIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessManagedMemoryStrategyType) -> str:
    return value


def deserialize_json(data: str) -> HarnessManagedMemoryStrategyType:
    return cast(HarnessManagedMemoryStrategyType, data)
