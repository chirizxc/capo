"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CancelPipelineExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.cancel_pipeline_execution_request_reason_string
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.workspace_name


class CancelPipelineExecutionRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the pipeline.</p>"""
    pipeline_execution_id: "capo_iotsitewise.types.id.ID"
    """<p>The unique identifier of the pipeline execution.</p>"""
    reason: NotRequired[
        "capo_iotsitewise.types.cancel_pipeline_execution_request_reason_string.CancelPipelineExecutionRequestReasonString"
    ]
    """<p>A message describing why the pipeline execution is being cancelled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelPipelineExecutionRequest) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> CancelPipelineExecutionRequest:
    out: CancelPipelineExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
