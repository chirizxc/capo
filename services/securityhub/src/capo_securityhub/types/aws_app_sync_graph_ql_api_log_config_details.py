"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAppSyncGraphQlApiLogConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsAppSyncGraphQlApiLogConfigDetails(TypedDict, closed=True):
    cloud_watch_logs_role_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the service role that AppSync assumes to publish to CloudWatch Logs in your account. </p>"""
    exclude_verbose_content: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Set to <code>TRUE</code> to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level. </p>"""
    field_log_level: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The field logging level. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAppSyncGraphQlApiLogConfigDetails) -> dict:
    out: dict = {}
    if "cloud_watch_logs_role_arn" in value:
        out["CloudWatchLogsRoleArn"] = value["cloud_watch_logs_role_arn"]
    if "exclude_verbose_content" in value:
        out["ExcludeVerboseContent"] = value["exclude_verbose_content"]
    if "field_log_level" in value:
        out["FieldLogLevel"] = value["field_log_level"]
    return out


def deserialize_json(data: dict) -> AwsAppSyncGraphQlApiLogConfigDetails:
    out: AwsAppSyncGraphQlApiLogConfigDetails = {}  # type: ignore[typeddict-item]
    if data.get("CloudWatchLogsRoleArn") is not None:
        out["cloud_watch_logs_role_arn"] = data["CloudWatchLogsRoleArn"]
    if data.get("ExcludeVerboseContent") is not None:
        out["exclude_verbose_content"] = data["ExcludeVerboseContent"]
    if data.get("FieldLogLevel") is not None:
        out["field_log_level"] = data["FieldLogLevel"]
    return out
