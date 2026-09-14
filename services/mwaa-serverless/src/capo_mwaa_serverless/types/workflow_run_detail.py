"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#WorkflowRunDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.generic_string
    import capo_mwaa_serverless.types.id_string
    import capo_mwaa_serverless.types.run_type
    import capo_mwaa_serverless.types.task_instance_ids
    import capo_mwaa_serverless.types.timestamp_value
    import capo_mwaa_serverless.types.version_id
    import capo_mwaa_serverless.types.workflow_arn
    import capo_mwaa_serverless.types.workflow_run_status


class WorkflowRunDetail(TypedDict, closed=True):
    workflow_arn: NotRequired["capo_mwaa_serverless.types.workflow_arn.WorkflowArn"]
    """<p>The Amazon Resource Name (ARN) of the workflow that contains this run.</p>"""
    workflow_version: NotRequired["capo_mwaa_serverless.types.version_id.VersionId"]
    """<p>The version of the workflow used for this run.</p>"""
    run_id: NotRequired["capo_mwaa_serverless.types.id_string.IdString"]
    """<p>The unique identifier of this workflow run.</p>"""
    run_type: NotRequired["capo_mwaa_serverless.types.run_type.RunType"]
    """<p>The type of workflow run.</p>"""
    started_on: NotRequired["capo_mwaa_serverless.types.timestamp_value.TimestampValue"]
    """<p>The timestamp when the workflow run started execution, in ISO 8601 date-time format.</p>"""
    created_at: NotRequired["capo_mwaa_serverless.types.timestamp_value.TimestampValue"]
    """<p>The timestamp when the workflow run was created, in ISO 8601 date-time format.</p>"""
    completed_on: NotRequired[
        "capo_mwaa_serverless.types.timestamp_value.TimestampValue"
    ]
    """<p>The timestamp when the workflow run completed execution, in ISO 8601 date-time format. This value is null if the run is not complete.</p>"""
    modified_at: NotRequired[
        "capo_mwaa_serverless.types.timestamp_value.TimestampValue"
    ]
    """<p>The timestamp when the workflow run was last modified, in ISO 8601 date-time format.</p>"""
    duration: NotRequired["int"]
    """<p>The total duration of the workflow run execution in seconds. This value is null if the run is not complete.</p>"""
    error_message: NotRequired[
        "capo_mwaa_serverless.types.generic_string.GenericString"
    ]
    """<p>The error message if the workflow run failed. This value is null if the run completed successfully.</p>"""
    task_instances: NotRequired[
        "capo_mwaa_serverless.types.task_instance_ids.TaskInstanceIds"
    ]
    """<p>A list of task instance IDs that are part of this workflow run.</p>"""
    run_state: NotRequired[
        "capo_mwaa_serverless.types.workflow_run_status.WorkflowRunStatus"
    ]
    """<p>The current execution state of the workflow run.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowRunDetail) -> dict:
    out: dict = {}
    if "workflow_arn" in value:
        out["WorkflowArn"] = value["workflow_arn"]
    if "workflow_version" in value:
        out["WorkflowVersion"] = value["workflow_version"]
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "run_type" in value:
        import capo_mwaa_serverless.types.run_type

        out["RunType"] = capo_mwaa_serverless.types.run_type.serialize_aws_json_1_0(
            value["run_type"]
        )
    if "started_on" in value:
        import capo_mwaa_serverless.types.timestamp_value

        out["StartedOn"] = (
            capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["started_on"]
            )
        )
    if "created_at" in value:
        import capo_mwaa_serverless.types.timestamp_value

        out["CreatedAt"] = (
            capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "completed_on" in value:
        import capo_mwaa_serverless.types.timestamp_value

        out["CompletedOn"] = (
            capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["completed_on"]
            )
        )
    if "modified_at" in value:
        import capo_mwaa_serverless.types.timestamp_value

        out["ModifiedAt"] = (
            capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["modified_at"]
            )
        )
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "task_instances" in value:
        import capo_mwaa_serverless.types.task_instance_ids

        out["TaskInstances"] = (
            capo_mwaa_serverless.types.task_instance_ids.serialize_aws_json_1_0(
                value["task_instances"]
            )
        )
    if "run_state" in value:
        import capo_mwaa_serverless.types.workflow_run_status

        out["RunState"] = (
            capo_mwaa_serverless.types.workflow_run_status.serialize_aws_json_1_0(
                value["run_state"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowRunDetail:
    out: WorkflowRunDetail = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowArn") is not None:
        out["workflow_arn"] = data["WorkflowArn"]
    if data.get("WorkflowVersion") is not None:
        out["workflow_version"] = data["WorkflowVersion"]
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    if data.get("RunType") is not None:
        import capo_mwaa_serverless.types.run_type

        out["run_type"] = capo_mwaa_serverless.types.run_type.deserialize_aws_json_1_0(
            data["RunType"]
        )
    if data.get("StartedOn") is not None:
        import capo_mwaa_serverless.types.timestamp_value

        out["started_on"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["StartedOn"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_mwaa_serverless.types.timestamp_value

        out["created_at"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if data.get("CompletedOn") is not None:
        import capo_mwaa_serverless.types.timestamp_value

        out["completed_on"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["CompletedOn"]
            )
        )
    if data.get("ModifiedAt") is not None:
        import capo_mwaa_serverless.types.timestamp_value

        out["modified_at"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["ModifiedAt"]
            )
        )
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("TaskInstances") is not None:
        import capo_mwaa_serverless.types.task_instance_ids

        out["task_instances"] = (
            capo_mwaa_serverless.types.task_instance_ids.deserialize_aws_json_1_0(
                data["TaskInstances"]
            )
        )
    if data.get("RunState") is not None:
        import capo_mwaa_serverless.types.workflow_run_status

        out["run_state"] = (
            capo_mwaa_serverless.types.workflow_run_status.deserialize_aws_json_1_0(
                data["RunState"]
            )
        )
    return out
