"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeEnrichmentJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.workspace_name


class DescribeEnrichmentJobRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the IoT SiteWise workspace containing the enrichment job.</p>"""
    job_id: "capo_iotsitewise.types.id.ID"
    """<p>The unique identifier of the enrichment job to retrieve. This is the jobId returned by CreateEnrichmentJob.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEnrichmentJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeEnrichmentJobRequest:
    out: DescribeEnrichmentJobRequest = {}  # type: ignore[typeddict-item]
    return out
