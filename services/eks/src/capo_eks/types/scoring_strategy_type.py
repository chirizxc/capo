"""Generated from Smithy shape ``com.amazonaws.eks#ScoringStrategyType``."""

from typing import Literal, TypeAlias, cast

"""<p>The scoring strategy type for the NodeResourcesFit scheduler plugin.</p>"""
ScoringStrategyType: TypeAlias = Literal[
    "LeastAllocated",
    "MostAllocated",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScoringStrategyType) -> str:
    return value


def deserialize_json(data: str) -> ScoringStrategyType:
    return cast(ScoringStrategyType, data)
