"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SyslogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_arn
    import capo_cloudwatch_logs.types.syslog_source_type
    import capo_cloudwatch_logs.types.timestamp
    import capo_cloudwatch_logs.types.vpc_endpoint_id


class SyslogConfiguration(TypedDict, closed=True):
    log_group_arn: NotRequired["capo_cloudwatch_logs.types.log_group_arn.LogGroupArn"]
    """<p>The ARN of the log group associated with this syslog configuration.</p>"""
    source_type: NotRequired[
        "capo_cloudwatch_logs.types.syslog_source_type.SyslogSourceType"
    ]
    """<p>The source type for the syslog configuration.</p>"""
    vpc_endpoint_id: NotRequired[
        "capo_cloudwatch_logs.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>The ID of the VPC endpoint used for syslog ingestion.</p>"""
    created_at: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time when the syslog configuration was created, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SyslogConfiguration) -> dict:
    out: dict = {}
    if "log_group_arn" in value:
        out["logGroupArn"] = value["log_group_arn"]
    if "source_type" in value:
        import capo_cloudwatch_logs.types.syslog_source_type

        out["sourceType"] = (
            capo_cloudwatch_logs.types.syslog_source_type.serialize_aws_json_1_1(
                value["source_type"]
            )
        )
    if "vpc_endpoint_id" in value:
        out["vpcEndpointId"] = value["vpc_endpoint_id"]
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SyslogConfiguration:
    out: SyslogConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("logGroupArn") is not None:
        out["log_group_arn"] = data["logGroupArn"]
    if data.get("sourceType") is not None:
        import capo_cloudwatch_logs.types.syslog_source_type

        out["source_type"] = (
            capo_cloudwatch_logs.types.syslog_source_type.deserialize_aws_json_1_1(
                data["sourceType"]
            )
        )
    if data.get("vpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["vpcEndpointId"]
    if data.get("createdAt") is not None:
        out["created_at"] = data["createdAt"]
    return out
