"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeDatasetExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.dataset_export_job_id
    import capo_iotsitewise.types.workspace_name


class DescribeDatasetExportJobRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace that contains the dataset export job.</p>"""
    job_id: "capo_iotsitewise.types.dataset_export_job_id.DatasetExportJobId"
    """<p>The unique identifier for the dataset export job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDatasetExportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDatasetExportJobRequest:
    out: DescribeDatasetExportJobRequest = {}  # type: ignore[typeddict-item]
    return out
