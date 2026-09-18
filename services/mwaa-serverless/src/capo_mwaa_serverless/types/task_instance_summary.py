"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#TaskInstanceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.generic_string
    import capo_mwaa_serverless.types.id_string
    import capo_mwaa_serverless.types.task_instance_status
    import capo_mwaa_serverless.types.version_id
    import capo_mwaa_serverless.types.workflow_arn


class TaskInstanceSummary(TypedDict, closed=True):
    workflow_arn: NotRequired["capo_mwaa_serverless.types.workflow_arn.WorkflowArn"]
    """<p>The Amazon Resource Name (ARN) of the workflow that contains this task instance.</p>"""
    workflow_version: NotRequired["capo_mwaa_serverless.types.version_id.VersionId"]
    """<p>The version of the workflow that contains this task instance.</p>"""
    run_id: NotRequired["capo_mwaa_serverless.types.id_string.IdString"]
    """<p>The unique identifier of the workflow run that contains this task instance.</p>"""
    task_instance_id: NotRequired["capo_mwaa_serverless.types.id_string.IdString"]
    """<p>The unique identifier of this task instance.</p>"""
    status: NotRequired[
        "capo_mwaa_serverless.types.task_instance_status.TaskInstanceStatus"
    ]
    """<p>The current status of the task instance.</p>"""
    duration_in_seconds: NotRequired["int"]
    """<p>The duration of the task instance execution in seconds. This value is null if the task is not complete.</p>"""
    operator_name: NotRequired[
        "capo_mwaa_serverless.types.generic_string.GenericString"
    ]
    """<p>The name of the Apache Airflow operator used for this task instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskInstanceSummary) -> dict:
    out: dict = {}
    if "workflow_arn" in value:
        out["WorkflowArn"] = value["workflow_arn"]
    if "workflow_version" in value:
        out["WorkflowVersion"] = value["workflow_version"]
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "task_instance_id" in value:
        out["TaskInstanceId"] = value["task_instance_id"]
    if "status" in value:
        import capo_mwaa_serverless.types.task_instance_status

        out["Status"] = (
            capo_mwaa_serverless.types.task_instance_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "duration_in_seconds" in value:
        out["DurationInSeconds"] = value["duration_in_seconds"]
    if "operator_name" in value:
        out["OperatorName"] = value["operator_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TaskInstanceSummary:
    out: TaskInstanceSummary = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowArn") is not None:
        out["workflow_arn"] = data["WorkflowArn"]
    if data.get("WorkflowVersion") is not None:
        out["workflow_version"] = data["WorkflowVersion"]
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    if data.get("TaskInstanceId") is not None:
        out["task_instance_id"] = data["TaskInstanceId"]
    if data.get("Status") is not None:
        import capo_mwaa_serverless.types.task_instance_status

        out["status"] = (
            capo_mwaa_serverless.types.task_instance_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("DurationInSeconds") is not None:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    if data.get("OperatorName") is not None:
        out["operator_name"] = data["OperatorName"]
    return out
