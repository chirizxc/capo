"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#UpdateWorkflowStepResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.step_id


class UpdateWorkflowStepResponse(TypedDict, closed=True):
    id: NotRequired["capo_migrationhuborchestrator.types.step_id.StepId"]
    """<p>The ID of the step.</p>"""
    step_group_id: NotRequired["str"]
    """<p>The ID of the step group.</p>"""
    workflow_id: NotRequired["str"]
    """<p>The ID of the migration workflow.</p>"""
    name: NotRequired["str"]
    """<p>The name of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkflowStepResponse) -> dict:
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


def deserialize_json(data: dict) -> UpdateWorkflowStepResponse:
    out: UpdateWorkflowStepResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("stepGroupId") is not None:
        out["step_group_id"] = data["stepGroupId"]
    if data.get("workflowId") is not None:
        out["workflow_id"] = data["workflowId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
