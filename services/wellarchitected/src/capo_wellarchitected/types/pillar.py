"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Pillar``."""

from typing import Literal, TypeAlias, cast

Pillar: TypeAlias = Literal[
    "COST_OPTIMIZATION",
    "SECURITY",
    "RESILIENCE",
    "PERFORMANCE",
    "OPERATIONAL_EXCELLENCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Pillar) -> str:
    return value


def deserialize_json(data: str) -> Pillar:
    return cast(Pillar, data)
