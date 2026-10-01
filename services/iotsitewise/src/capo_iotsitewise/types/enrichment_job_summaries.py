"""Generated from Smithy shape ``com.amazonaws.iotsitewise#EnrichmentJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.enrichment_job_summary

EnrichmentJobSummaries: TypeAlias = list[
    "capo_iotsitewise.types.enrichment_job_summary.EnrichmentJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnrichmentJobSummaries) -> list:
    import capo_iotsitewise.types.enrichment_job_summary

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.enrichment_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnrichmentJobSummaries:
    import capo_iotsitewise.types.enrichment_job_summary

    out: EnrichmentJobSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iotsitewise.types.enrichment_job_summary.deserialize_json(item))
    return out
