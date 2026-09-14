"""Generated from Smithy shape ``com.amazonaws.glue#CancelMLTaskRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string
    import capo_glue.types.task_status_type


class CancelMLTaskRunResponse(TypedDict, closed=True):
    transform_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The unique identifier of the machine learning transform.</p>"""
    task_run_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The unique identifier for the task run.</p>"""
    status: NotRequired["capo_glue.types.task_status_type.TaskStatusType"]
    """<p>The status for this run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelMLTaskRunResponse) -> dict:
    out: dict = {}
    if "transform_id" in value:
        out["TransformId"] = value["transform_id"]
    if "task_run_id" in value:
        out["TaskRunId"] = value["task_run_id"]
    if "status" in value:
        import capo_glue.types.task_status_type

        out["Status"] = capo_glue.types.task_status_type.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelMLTaskRunResponse:
    out: CancelMLTaskRunResponse = {}  # type: ignore[typeddict-item]
    if data.get("TransformId") is not None:
        out["transform_id"] = data["TransformId"]
    if data.get("TaskRunId") is not None:
        out["task_run_id"] = data["TaskRunId"]
    if data.get("Status") is not None:
        import capo_glue.types.task_status_type

        out["status"] = capo_glue.types.task_status_type.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
