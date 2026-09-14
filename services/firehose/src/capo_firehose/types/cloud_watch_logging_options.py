"""Generated from Smithy shape ``com.amazonaws.firehose#CloudWatchLoggingOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.boolean_object
    import capo_firehose.types.log_group_name
    import capo_firehose.types.log_stream_name


class CloudWatchLoggingOptions(TypedDict, closed=True):
    enabled: NotRequired["capo_firehose.types.boolean_object.BooleanObject"]
    """<p>Enables or disables CloudWatch logging.</p>"""
    log_group_name: NotRequired["capo_firehose.types.log_group_name.LogGroupName"]
    """<p>The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.</p>"""
    log_stream_name: NotRequired["capo_firehose.types.log_stream_name.LogStreamName"]
    """<p>The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLoggingOptions) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "log_group_name" in value:
        out["LogGroupName"] = value["log_group_name"]
    if "log_stream_name" in value:
        out["LogStreamName"] = value["log_stream_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchLoggingOptions:
    out: CloudWatchLoggingOptions = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("LogGroupName") is not None:
        out["log_group_name"] = data["LogGroupName"]
    if data.get("LogStreamName") is not None:
        out["log_stream_name"] = data["LogStreamName"]
    return out
