"""Generated from Smithy shape ``com.amazonaws.personalize#DatasetImportJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.boolean
    import capo_personalize.types.data_source
    import capo_personalize.types.date
    import capo_personalize.types.failure_reason
    import capo_personalize.types.import_mode
    import capo_personalize.types.name
    import capo_personalize.types.status


class DatasetImportJob(TypedDict, closed=True):
    job_name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the import job.</p>"""
    dataset_import_job_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The ARN of the dataset import job.</p>"""
    dataset_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset that receives the imported data.</p>"""
    data_source: NotRequired["capo_personalize.types.data_source.DataSource"]
    """<p>The Amazon S3 bucket that contains the training data to import.</p>"""
    role_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The ARN of the IAM role that has permissions to read from the Amazon S3 data source.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The status of the dataset import job.</p> <p>A dataset import job can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> </ul>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The creation date and time (in Unix time) of the dataset import job.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) the dataset was last updated.</p>"""
    failure_reason: NotRequired["capo_personalize.types.failure_reason.FailureReason"]
    """<p>If a dataset import job fails, provides the reason why.</p>"""
    import_mode: NotRequired["capo_personalize.types.import_mode.ImportMode"]
    """<p>The import mode used by the dataset import job to import new records.</p>"""
    publish_attribution_metrics_to_s3: NotRequired[
        "capo_personalize.types.boolean.Boolean"
    ]
    """<p>Whether the job publishes metrics to Amazon S3 for a metric attribution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetImportJob) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "dataset_import_job_arn" in value:
        out["datasetImportJobArn"] = value["dataset_import_job_arn"]
    if "dataset_arn" in value:
        out["datasetArn"] = value["dataset_arn"]
    if "data_source" in value:
        import capo_personalize.types.data_source

        out["dataSource"] = capo_personalize.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
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
    if "import_mode" in value:
        import capo_personalize.types.import_mode

        out["importMode"] = capo_personalize.types.import_mode.serialize_aws_json_1_1(
            value["import_mode"]
        )
    if "publish_attribution_metrics_to_s3" in value:
        out["publishAttributionMetricsToS3"] = value[
            "publish_attribution_metrics_to_s3"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetImportJob:
    out: DatasetImportJob = {}  # type: ignore[typeddict-item]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    if data.get("datasetImportJobArn") is not None:
        out["dataset_import_job_arn"] = data["datasetImportJobArn"]
    if data.get("datasetArn") is not None:
        out["dataset_arn"] = data["datasetArn"]
    if data.get("dataSource") is not None:
        import capo_personalize.types.data_source

        out["data_source"] = (
            capo_personalize.types.data_source.deserialize_aws_json_1_1(
                data["dataSource"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
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
    if data.get("importMode") is not None:
        import capo_personalize.types.import_mode

        out["import_mode"] = (
            capo_personalize.types.import_mode.deserialize_aws_json_1_1(
                data["importMode"]
            )
        )
    if data.get("publishAttributionMetricsToS3") is not None:
        out["publish_attribution_metrics_to_s3"] = data["publishAttributionMetricsToS3"]
    return out
