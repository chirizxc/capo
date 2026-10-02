"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetEnrichmentStatus``."""

from typing import Literal, TypeAlias, cast

DatasetEnrichmentStatus: TypeAlias = Literal[
    "FULLY_ENRICHED",
    "PARTIALLY_ENRICHED",
    "NOT_ENRICHED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetEnrichmentStatus) -> str:
    return value


def deserialize_json(data: str) -> DatasetEnrichmentStatus:
    return cast(DatasetEnrichmentStatus, data)
