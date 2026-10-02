"""Generated from Smithy shape ``com.amazonaws.kinesis#ChannelLoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.cloud_watch_logs


class ChannelLoggingConfiguration(TypedDict, closed=True):
    cloud_watch_logs: "capo_kinesis.types.cloud_watch_logs.CloudWatchLogs"
    """<p>The Amazon CloudWatch Logs settings for the channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelLoggingConfiguration) -> dict:
    out: dict = {}
    import capo_kinesis.types.cloud_watch_logs

    out["CloudWatchLogs"] = capo_kinesis.types.cloud_watch_logs.serialize_aws_json_1_1(
        value["cloud_watch_logs"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ChannelLoggingConfiguration:
    out: ChannelLoggingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CloudWatchLogs") is not None:
        import capo_kinesis.types.cloud_watch_logs

        out["cloud_watch_logs"] = (
            capo_kinesis.types.cloud_watch_logs.deserialize_aws_json_1_1(
                data["CloudWatchLogs"]
            )
        )
    else:
        raise DeserializationError(
            "ChannelLoggingConfiguration.cloud_watch_logs required"
        )
    return out
