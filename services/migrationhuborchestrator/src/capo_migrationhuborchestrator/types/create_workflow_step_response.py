"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#CreateWorkflowStepResponse``."""

from typing_extensions import NotRequired, TypedDict


class CreateWorkflowStepResponse(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>The ID of the step.</p>"""
    step_group_id: NotRequired["str"]
    """<p>The ID of the step group.</p>"""
    workflow_id: NotRequired["str"]
    """<p>The ID of the migration workflow.</p>"""
    name: NotRequired["str"]
    """<p>The name of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowStepResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "step_group_id" in value:
        out["stepGroupId"] = value["step_group_id"]
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateWorkflowStepResponse:
    out: CreateWorkflowStepResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("stepGroupId") is not None:
        out["step_group_id"] = data["stepGroupId"]
    if data.get("workflowId") is not None:
        out["workflow_id"] = data["workflowId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
