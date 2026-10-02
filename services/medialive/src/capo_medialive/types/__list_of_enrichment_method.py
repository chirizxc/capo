"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfEnrichmentMethod``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.enrichment_method

__listOfEnrichmentMethod: TypeAlias = list[
    "capo_medialive.types.enrichment_method.EnrichmentMethod"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfEnrichmentMethod) -> list:
    import capo_medialive.types.enrichment_method

    out: list = []
    for item in value:
        out.append(capo_medialive.types.enrichment_method.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfEnrichmentMethod:
    import capo_medialive.types.enrichment_method

    out: __listOfEnrichmentMethod = []
    for item in data:
        if item is None:
            continue
        out.append(capo_medialive.types.enrichment_method.deserialize_json(item))
    return out
