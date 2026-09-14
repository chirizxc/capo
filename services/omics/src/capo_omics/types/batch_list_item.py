"""Generated from Smithy shape ``com.amazonaws.omics#BatchListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.batch_id
    import capo_omics.types.batch_name
    import capo_omics.types.batch_status
    import capo_omics.types.batch_timestamp
    import capo_omics.types.workflow_id


class BatchListItem(TypedDict, closed=True):
    id: NotRequired["capo_omics.types.batch_id.BatchId"]
    """<p>The batch identifier.</p>"""
    name: NotRequired["capo_omics.types.batch_name.BatchName"]
    """<p>The batch name.</p>"""
    status: NotRequired["capo_omics.types.batch_status.BatchStatus"]
    """<p>The current batch status.</p>"""
    created_at: NotRequired["capo_omics.types.batch_timestamp.BatchTimestamp"]
    """<p>The timestamp when the batch was created.</p>"""
    total_runs: NotRequired["int"]
    """<p>The total number of runs in the batch.</p>"""
    workflow_id: NotRequired["capo_omics.types.workflow_id.WorkflowId"]
    """<p>The identifier of the workflow used for the batch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchListItem) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "created_at" in value:
        import capo_omics.types.batch_timestamp

        out["createdAt"] = capo_omics.types.batch_timestamp.serialize_json(
            value["created_at"]
        )
    if "total_runs" in value:
        out["totalRuns"] = value["total_runs"]
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    return out


def deserialize_json(data: dict) -> BatchListItem:
    out: BatchListItem = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("createdAt") is not None:
        import capo_omics.types.batch_timestamp

        out["created_at"] = capo_omics.types.batch_timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("totalRuns") is not None:
        out["total_runs"] = data["totalRuns"]
    if data.get("workflowId") is not None:
        out["workflow_id"] = data["workflowId"]
    return out
