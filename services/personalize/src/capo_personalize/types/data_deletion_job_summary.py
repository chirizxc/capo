"""Generated from Smithy shape ``com.amazonaws.personalize#DataDeletionJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.date
    import capo_personalize.types.failure_reason
    import capo_personalize.types.name
    import capo_personalize.types.status


class DataDeletionJobSummary(TypedDict, closed=True):
    data_deletion_job_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the data deletion job.</p>"""
    dataset_group_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset group the job deleted records from.</p>"""
    job_name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the data deletion job.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The status of the data deletion job.</p> <p>A data deletion job can have one of the following statuses:</p> <ul> <li> <p>PENDING > IN_PROGRESS > COMPLETED -or- FAILED</p> </li> </ul>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The creation date and time (in Unix time) of the data deletion job.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) the data deletion job was last updated.</p>"""
    failure_reason: NotRequired["capo_personalize.types.failure_reason.FailureReason"]
    """<p>If a data deletion job fails, provides the reason why.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataDeletionJobSummary) -> dict:
    out: dict = {}
    if "data_deletion_job_arn" in value:
        out["dataDeletionJobArn"] = value["data_deletion_job_arn"]
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "status" in value:
        out["status"] = value["status"]
    if "creation_date_time" in value:
        import capo_personalize.types.date

        out["creationDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_personalize.types.date

        out["lastUpdatedDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["last_updated_date_time"]
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataDeletionJobSummary:
    out: DataDeletionJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("dataDeletionJobArn") is not None:
        out["data_deletion_job_arn"] = data["dataDeletionJobArn"]
    if data.get("datasetGroupArn") is not None:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("creationDateTime") is not None:
        import capo_personalize.types.date

        out["creation_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if data.get("lastUpdatedDateTime") is not None:
        import capo_personalize.types.date

        out["last_updated_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    return out
