"""Generated from Smithy shape ``com.amazonaws.kafka#ChannelInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.__timestamp_iso8601
    import capo_kafka.types.channel_destination_type
    import capo_kafka.types.channel_status


class ChannelInfo(TypedDict, closed=True):
    channel_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the channel.</p>"""
    channel_name: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The name of the channel.</p>"""
    status: NotRequired["capo_kafka.types.channel_status.ChannelStatus"]
    """<p>The current lifecycle state of the channel.</p>"""
    creation_time: NotRequired[
        "capo_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when the channel was created.</p>"""
    destination_type: NotRequired[
        "capo_kafka.types.channel_destination_type.ChannelDestinationType"
    ]
    """<p>The type of destination configured for the channel.</p>"""
    cluster_operation_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the in-flight cluster operation. Returned only while the channel is in CREATING, UPDATING, or DELETING.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelInfo) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["channelArn"] = value["channel_arn"]
    if "channel_name" in value:
        out["channelName"] = value["channel_name"]
    if "status" in value:
        import capo_kafka.types.channel_status

        out["status"] = capo_kafka.types.channel_status.serialize_json(value["status"])
    if "creation_time" in value:
        import capo_kafka.types.__timestamp_iso8601

        out["creationTime"] = capo_kafka.types.__timestamp_iso8601.serialize_json(
            value["creation_time"]
        )
    if "destination_type" in value:
        import capo_kafka.types.channel_destination_type

        out["destinationType"] = (
            capo_kafka.types.channel_destination_type.serialize_json(
                value["destination_type"]
            )
        )
    if "cluster_operation_arn" in value:
        out["clusterOperationArn"] = value["cluster_operation_arn"]
    return out


def deserialize_json(data: dict) -> ChannelInfo:
    out: ChannelInfo = {}  # type: ignore[typeddict-item]
    if data.get("channelArn") is not None:
        out["channel_arn"] = data["channelArn"]
    if data.get("channelName") is not None:
        out["channel_name"] = data["channelName"]
    if data.get("status") is not None:
        import capo_kafka.types.channel_status

        out["status"] = capo_kafka.types.channel_status.deserialize_json(data["status"])
    if data.get("creationTime") is not None:
        import capo_kafka.types.__timestamp_iso8601

        out["creation_time"] = capo_kafka.types.__timestamp_iso8601.deserialize_json(
            data["creationTime"]
        )
    if data.get("destinationType") is not None:
        import capo_kafka.types.channel_destination_type

        out["destination_type"] = (
            capo_kafka.types.channel_destination_type.deserialize_json(
                data["destinationType"]
            )
        )
    if data.get("clusterOperationArn") is not None:
        out["cluster_operation_arn"] = data["clusterOperationArn"]
    return out
