"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListDatasetExportJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.dataset_export_job_filter
    import capo_iotsitewise.types.list_export_jobs_max_results
    import capo_iotsitewise.types.list_export_jobs_next_token
    import capo_iotsitewise.types.workspace_name


class ListDatasetExportJobsRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace whose dataset export jobs should be listed.</p>"""
    filter: NotRequired[
        "capo_iotsitewise.types.dataset_export_job_filter.DatasetExportJobFilter"
    ]
    """<p>The optional filter that returns only jobs matching the given filter value. Defaults to ALL.</p>"""
    max_results: NotRequired[
        "capo_iotsitewise.types.list_export_jobs_max_results.ListExportJobsMaxResults"
    ]
    """<p>The maximum number of results to return for each paginated request.</p>"""
    next_token: NotRequired[
        "capo_iotsitewise.types.list_export_jobs_next_token.ListExportJobsNextToken"
    ]
    """<p>The token to be used for the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetExportJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDatasetExportJobsRequest:
    out: ListDatasetExportJobsRequest = {}  # type: ignore[typeddict-item]
    return out
