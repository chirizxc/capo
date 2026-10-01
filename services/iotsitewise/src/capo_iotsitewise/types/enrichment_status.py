"""Generated from Smithy shape ``com.amazonaws.iotsitewise#EnrichmentStatus``."""

from typing import Literal, TypeAlias, cast

EnrichmentStatus: TypeAlias = Literal[
    "ENRICHED",
    "NOT_ENRICHED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EnrichmentStatus) -> str:
    return value


def deserialize_json(data: str) -> EnrichmentStatus:
    return cast(EnrichmentStatus, data)
