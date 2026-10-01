"""Generated from Smithy shape ``com.amazonaws.iotsitewise#EnrichmentJobStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Status of an enrichment job throughout its lifecycle.</p> <p>Status progression: PENDING → RUNNING → {COMPLETED, FAILED, TIMED_OUT, CANCELLED}</p> <ul> <li>PENDING: Job has been accepted and is waiting to start processing</li> <li>RUNNING: Job is actively processing video data to generate embeddings</li> <li>COMPLETED: Job finished successfully; embeddings are available in IoT SiteWise</li> <li>FAILED: Job encountered an error during processing</li> <li>TIMED_OUT: Job exceeded the maximum processing time limit</li> <li>CANCELLED: Job was cancelled via CancelEnrichmentJob</li> </ul> <p>Terminal states (job will not change status): COMPLETED, FAILED, TIMED_OUT, CANCELLED</p>"""
EnrichmentJobStatus: TypeAlias = Literal[
    "PENDING",
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "TIMED_OUT",
    "CANCELLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EnrichmentJobStatus) -> str:
    return value


def deserialize_json(data: str) -> EnrichmentJobStatus:
    return cast(EnrichmentJobStatus, data)
