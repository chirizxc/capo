"""Generated from Smithy shape ``com.amazonaws.kafka#ChannelLoggingInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.cloud_watch_logs
    import capo_kafka.types.firehose
    import capo_kafka.types.s3


class ChannelLoggingInfo(TypedDict, closed=True):
    cloud_watch_logs: NotRequired["capo_kafka.types.cloud_watch_logs.CloudWatchLogs"]
    """<p>Details of the CloudWatch Logs destination for Channel logs.</p>"""
    firehose: NotRequired["capo_kafka.types.firehose.Firehose"]
    """<p>Details of the Kinesis Data Firehose delivery stream that is the destination for Channel logs.</p>"""
    s3: NotRequired["capo_kafka.types.s3.S3"]
    """<p>Details of the Amazon S3 destination for Channel logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelLoggingInfo) -> dict:
    out: dict = {}
    if "cloud_watch_logs" in value:
        import capo_kafka.types.cloud_watch_logs

        out["cloudWatchLogs"] = capo_kafka.types.cloud_watch_logs.serialize_json(
            value["cloud_watch_logs"]
        )
    if "firehose" in value:
        import capo_kafka.types.firehose

        out["firehose"] = capo_kafka.types.firehose.serialize_json(value["firehose"])
    if "s3" in value:
        import capo_kafka.types.s3

        out["s3"] = capo_kafka.types.s3.serialize_json(value["s3"])
    return out


def deserialize_json(data: dict) -> ChannelLoggingInfo:
    out: ChannelLoggingInfo = {}  # type: ignore[typeddict-item]
    if data.get("cloudWatchLogs") is not None:
        import capo_kafka.types.cloud_watch_logs

        out["cloud_watch_logs"] = capo_kafka.types.cloud_watch_logs.deserialize_json(
            data["cloudWatchLogs"]
        )
    if data.get("firehose") is not None:
        import capo_kafka.types.firehose

        out["firehose"] = capo_kafka.types.firehose.deserialize_json(data["firehose"])
    if data.get("s3") is not None:
        import capo_kafka.types.s3

        out["s3"] = capo_kafka.types.s3.deserialize_json(data["s3"])
    return out
