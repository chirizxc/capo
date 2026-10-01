"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#LoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn


class LoggingConfiguration(TypedDict, closed=True):
    s3_bucket_name: NotRequired["str"]
    """<p>The name of the S3 bucket for log delivery.</p>"""
    cloud_watch_log_group_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    """<p>The ARN of the CloudWatch Logs log group for log delivery.</p>"""
    log_schema_version: NotRequired["str"]
    """<p>The version of the log schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingConfiguration) -> dict:
    out: dict = {}
    if "s3_bucket_name" in value:
        out["s3BucketName"] = value["s3_bucket_name"]
    if "cloud_watch_log_group_arn" in value:
        out["cloudWatchLogGroupArn"] = value["cloud_watch_log_group_arn"]
    if "log_schema_version" in value:
        out["logSchemaVersion"] = value["log_schema_version"]
    return out


def deserialize_json(data: dict) -> LoggingConfiguration:
    out: LoggingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("s3BucketName") is not None:
        out["s3_bucket_name"] = data["s3BucketName"]
    if data.get("cloudWatchLogGroupArn") is not None:
        out["cloud_watch_log_group_arn"] = data["cloudWatchLogGroupArn"]
    if data.get("logSchemaVersion") is not None:
        out["log_schema_version"] = data["logSchemaVersion"]
    return out
