"""Generated from Smithy shape ``com.amazonaws.securityhub#CloudWatchLogsLogGroupArnConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class CloudWatchLogsLogGroupArnConfigDetails(TypedDict, closed=True):
    cloud_watch_logs_log_group_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ARN of the CloudWatch Logs log group that Route 53 is publishing logs to.</p>"""
    hosted_zone_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the hosted zone that CloudWatch Logs is logging queries for. </p>"""
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID for a DNS query logging configuration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogsLogGroupArnConfigDetails) -> dict:
    out: dict = {}
    if "cloud_watch_logs_log_group_arn" in value:
        out["CloudWatchLogsLogGroupArn"] = value["cloud_watch_logs_log_group_arn"]
    if "hosted_zone_id" in value:
        out["HostedZoneId"] = value["hosted_zone_id"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CloudWatchLogsLogGroupArnConfigDetails:
    out: CloudWatchLogsLogGroupArnConfigDetails = {}  # type: ignore[typeddict-item]
    if data.get("CloudWatchLogsLogGroupArn") is not None:
        out["cloud_watch_logs_log_group_arn"] = data["CloudWatchLogsLogGroupArn"]
    if data.get("HostedZoneId") is not None:
        out["hosted_zone_id"] = data["HostedZoneId"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    return out
