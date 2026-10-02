"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ClusteringFrequency``."""

from typing import Literal, TypeAlias, cast

ClusteringFrequency: TypeAlias = Literal[
    "DAILY",
    "WEEKLY",
    "MONTHLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClusteringFrequency) -> str:
    return value


def deserialize_json(data: str) -> ClusteringFrequency:
    return cast(ClusteringFrequency, data)
