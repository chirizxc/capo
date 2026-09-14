"""Generated from Smithy shape ``com.amazonaws.omics#CreateWorkflowVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.tag_map
    import capo_omics.types.workflow_id
    import capo_omics.types.workflow_status
    import capo_omics.types.workflow_uuid
    import capo_omics.types.workflow_version_arn
    import capo_omics.types.workflow_version_name


class CreateWorkflowVersionResponse(TypedDict, closed=True):
    arn: NotRequired["capo_omics.types.workflow_version_arn.WorkflowVersionArn"]
    """<p>ARN of the workflow version.</p>"""
    workflow_id: NotRequired["capo_omics.types.workflow_id.WorkflowId"]
    """<p>The workflow's ID.</p>"""
    version_name: NotRequired[
        "capo_omics.types.workflow_version_name.WorkflowVersionName"
    ]
    """<p>The workflow version name.</p>"""
    status: NotRequired["capo_omics.types.workflow_status.WorkflowStatus"]
    """<p>The workflow version status.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>The workflow version's tags.</p>"""
    uuid: NotRequired["capo_omics.types.workflow_uuid.WorkflowUuid"]
    """<p>The universally unique identifier (UUID) value for this workflow version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowVersionResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    if "version_name" in value:
        out["versionName"] = value["version_name"]
    if "status" in value:
        out["status"] = value["status"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    if "uuid" in value:
        out["uuid"] = value["uuid"]
    return out


def deserialize_json(data: dict) -> CreateWorkflowVersionResponse:
    out: CreateWorkflowVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("workflowId") is not None:
        out["workflow_id"] = data["workflowId"]
    if data.get("versionName") is not None:
        out["version_name"] = data["versionName"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    if data.get("uuid") is not None:
        out["uuid"] = data["uuid"]
    return out
