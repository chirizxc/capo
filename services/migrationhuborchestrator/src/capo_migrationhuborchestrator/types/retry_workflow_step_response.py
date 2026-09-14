"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#RetryWorkflowStepResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.step_status


class RetryWorkflowStepResponse(TypedDict, closed=True):
    step_group_id: NotRequired["str"]
    """<p>The ID of the step group.</p>"""
    workflow_id: NotRequired["str"]
    """<p>The ID of the migration workflow.</p>"""
    id: NotRequired["str"]
    """<p>The ID of the step.</p>"""
    status: NotRequired["capo_migrationhuborchestrator.types.step_status.StepStatus"]
    """<p>The status of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryWorkflowStepResponse) -> dict:
    out: dict = {}
    if "step_group_id" in value:
        out["stepGroupId"] = value["step_group_id"]
    if "workflow_id" in value:
        out["workflowId"] = value["workflow_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> RetryWorkflowStepResponse:
    out: RetryWorkflowStepResponse = {}  # type: ignore[typeddict-item]
    if data.get("stepGroupId") is not None:
        out["step_group_id"] = data["stepGroupId"]
    if data.get("workflowId") is not None:
        out["workflow_id"] = data["workflowId"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
