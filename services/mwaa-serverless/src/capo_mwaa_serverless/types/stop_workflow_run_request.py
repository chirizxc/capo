"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#StopWorkflowRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mwaa_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.id_string
    import capo_mwaa_serverless.types.workflow_arn


class StopWorkflowRunRequest(TypedDict, closed=True):
    workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow that contains the run you want to stop.</p>"""
    run_id: "capo_mwaa_serverless.types.id_string.IdString"
    """<p>The unique identifier of the workflow run to stop.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopWorkflowRunRequest) -> dict:
    out: dict = {}
    out["WorkflowArn"] = value["workflow_arn"]
    out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StopWorkflowRunRequest:
    out: StopWorkflowRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowArn") is not None:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        raise DeserializationError("StopWorkflowRunRequest.workflow_arn required")
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    else:
        raise DeserializationError("StopWorkflowRunRequest.run_id required")
    return out
