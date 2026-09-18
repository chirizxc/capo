"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#GetTaskInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mwaa_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.id_string
    import capo_mwaa_serverless.types.workflow_arn


class GetTaskInstanceRequest(TypedDict, closed=True):
    workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow that contains the task instance.</p>"""
    task_instance_id: "capo_mwaa_serverless.types.id_string.IdString"
    """<p>The unique identifier of the task instance to retrieve.</p>"""
    run_id: "capo_mwaa_serverless.types.id_string.IdString"
    """<p>The unique identifier of the workflow run that contains the task instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTaskInstanceRequest) -> dict:
    out: dict = {}
    out["WorkflowArn"] = value["workflow_arn"]
    out["TaskInstanceId"] = value["task_instance_id"]
    out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTaskInstanceRequest:
    out: GetTaskInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowArn") is not None:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        raise DeserializationError("GetTaskInstanceRequest.workflow_arn required")
    if data.get("TaskInstanceId") is not None:
        out["task_instance_id"] = data["TaskInstanceId"]
    else:
        raise DeserializationError("GetTaskInstanceRequest.task_instance_id required")
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    else:
        raise DeserializationError("GetTaskInstanceRequest.run_id required")
    return out
