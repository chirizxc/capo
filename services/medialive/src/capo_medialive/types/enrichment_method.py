"""Generated from Smithy shape ``com.amazonaws.medialive#EnrichmentMethod``."""

from typing import Literal, TypeAlias, cast

"""A Contextual Metadata Enrichment method. Each value selects a strategy for enriching the channel's output with contextual metadata derived from the Elemental Inference feed. SCTE35_ELEMENTAL_INFERENCE_QUERY_PARAMS enriches outbound SCTE-35 messages with query parameters that downstream systems can use to call the Elemental Inference GetMetadata API."""
EnrichmentMethod: TypeAlias = Literal["SCTE35_ELEMENTAL_INFERENCE_QUERY_PARAMS",]


# --- restJson1 ser/de ---
def serialize_json(value: EnrichmentMethod) -> str:
    return value


def deserialize_json(data: str) -> EnrichmentMethod:
    return cast(EnrichmentMethod, data)
