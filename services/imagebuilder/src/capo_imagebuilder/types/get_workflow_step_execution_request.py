"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetWorkflowStepExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.workflow_step_execution_id


class GetWorkflowStepExecutionRequest(TypedDict, closed=True):
    step_execution_id: (
        "capo_imagebuilder.types.workflow_step_execution_id.WorkflowStepExecutionId"
    )
    """<p>The unique identifier for the runtime instance of the workflow step that you want to get runtime details for. To get the identifiers for the steps that ran in a workflow, call <a>ListWorkflowStepExecutions</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowStepExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWorkflowStepExecutionRequest:
    out: GetWorkflowStepExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
