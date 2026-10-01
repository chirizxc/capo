"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ProspectingTaskSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.prospecting_task_arn
    import capo_partnercentral_selling.types.prospecting_task_identifier
    import capo_partnercentral_selling.types.task_name


class ProspectingTaskSummary(TypedDict, closed=True):
    task_id: "capo_partnercentral_selling.types.prospecting_task_identifier.ProspectingTaskIdentifier"
    """<p>The unique identifier of the task. Use this value with <code>GetProspectingFromEngagementTask</code> to retrieve full task details.</p>"""
    task_arn: (
        "capo_partnercentral_selling.types.prospecting_task_arn.ProspectingTaskArn"
    )
    """<p>The Amazon Resource Name (ARN) of the task.</p>"""
    task_name: "capo_partnercentral_selling.types.task_name.TaskName"
    """<p>The descriptive name of the task provided when it was created.</p>"""
    start_time: "capo_partnercentral_selling.types.date_time.DateTime"
    """<p>The timestamp indicating when the task was initiated. The format follows ISO 8601 date-time notation.</p>"""
    end_time: NotRequired["capo_partnercentral_selling.types.date_time.DateTime"]
    """<p>The timestamp indicating when the task finished processing. This field is absent if the task is still in progress. The format follows ISO 8601 date-time notation.</p>"""
    total_engagement_count: "int"
    """<p>The total number of engagements included in the task.</p>"""
    completed_engagement_count: "int"
    """<p>The number of engagements that have been successfully converted into prospecting leads.</p>"""
    failed_engagement_count: "int"
    """<p>The number of engagements that failed to be converted. Retrieve the full task details using <code>GetProspectingFromEngagementTask</code> for per-engagement error information.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProspectingTaskSummary) -> dict:
    out: dict = {}
    out["TaskId"] = value["task_id"]
    out["TaskArn"] = value["task_arn"]
    out["TaskName"] = value["task_name"]
    import capo_partnercentral_selling.types.date_time

    out["StartTime"] = (
        capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
            value["start_time"]
        )
    )
    if "end_time" in value:
        import capo_partnercentral_selling.types.date_time

        out["EndTime"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["end_time"]
            )
        )
    out["TotalEngagementCount"] = value.get("total_engagement_count", 0)
    out["CompletedEngagementCount"] = value["completed_engagement_count"]
    out["FailedEngagementCount"] = value["failed_engagement_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProspectingTaskSummary:
    out: ProspectingTaskSummary = {}  # type: ignore[typeddict-item]
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    else:
        raise DeserializationError("ProspectingTaskSummary.task_id required")
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    else:
        raise DeserializationError("ProspectingTaskSummary.task_arn required")
    if data.get("TaskName") is not None:
        out["task_name"] = data["TaskName"]
    else:
        raise DeserializationError("ProspectingTaskSummary.task_name required")
    if data.get("StartTime") is not None:
        import capo_partnercentral_selling.types.date_time

        out["start_time"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("ProspectingTaskSummary.start_time required")
    if data.get("EndTime") is not None:
        import capo_partnercentral_selling.types.date_time

        out["end_time"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["EndTime"]
            )
        )
    if data.get("TotalEngagementCount") is not None:
        out["total_engagement_count"] = data["TotalEngagementCount"]
    else:
        out["total_engagement_count"] = 0
    if data.get("CompletedEngagementCount") is not None:
        out["completed_engagement_count"] = data["CompletedEngagementCount"]
    else:
        raise DeserializationError(
            "ProspectingTaskSummary.completed_engagement_count required"
        )
    if data.get("FailedEngagementCount") is not None:
        out["failed_engagement_count"] = data["FailedEngagementCount"]
    else:
        raise DeserializationError(
            "ProspectingTaskSummary.failed_engagement_count required"
        )
    return out
