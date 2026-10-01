"""Generated from Smithy shape ``com.amazonaws.kinesis#ChannelLoggingUpdateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.cloud_watch_logs_update_input


class ChannelLoggingUpdateInput(TypedDict, closed=True):
    cloud_watch_logs: (
        "capo_kinesis.types.cloud_watch_logs_update_input.CloudWatchLogsUpdateInput"
    )
    """<p>The updated Amazon CloudWatch Logs settings, including whether logging is enabled and the target log group and log stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelLoggingUpdateInput) -> dict:
    out: dict = {}
    import capo_kinesis.types.cloud_watch_logs_update_input

    out["CloudWatchLogs"] = (
        capo_kinesis.types.cloud_watch_logs_update_input.serialize_aws_json_1_1(
            value["cloud_watch_logs"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ChannelLoggingUpdateInput:
    out: ChannelLoggingUpdateInput = {}  # type: ignore[typeddict-item]
    if data.get("CloudWatchLogs") is not None:
        import capo_kinesis.types.cloud_watch_logs_update_input

        out["cloud_watch_logs"] = (
            capo_kinesis.types.cloud_watch_logs_update_input.deserialize_aws_json_1_1(
                data["CloudWatchLogs"]
            )
        )
    else:
        raise DeserializationError(
            "ChannelLoggingUpdateInput.cloud_watch_logs required"
        )
    return out
