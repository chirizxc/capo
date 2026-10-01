"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__list_of_topic_configuration
    import capo_kafka.types.__map_of__string
    import capo_kafka.types.__string
    import capo_kafka.types.__timestamp_iso8601
    import capo_kafka.types.channel_destination_type
    import capo_kafka.types.channel_logging_info
    import capo_kafka.types.channel_state_info
    import capo_kafka.types.channel_status
    import capo_kafka.types.encryption_configuration
    import capo_kafka.types.iceberg_destination_configuration
    import capo_kafka.types.s3_destination_configuration


class DescribeChannelResponse(TypedDict, closed=True):
    channel_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the channel.</p>"""
    channel_name: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The name of the channel.</p>"""
    encryption_configuration: NotRequired[
        "capo_kafka.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration applied to the channel.</p>"""
    iceberg_destination_configuration: NotRequired[
        "capo_kafka.types.iceberg_destination_configuration.IcebergDestinationConfiguration"
    ]
    """<p>The Apache Iceberg destination for the channel, if configured.</p>"""
    s3_destination_configuration: NotRequired[
        "capo_kafka.types.s3_destination_configuration.S3DestinationConfiguration"
    ]
    """<p>The Amazon S3 destination for the channel, if configured.</p>"""
    status: NotRequired["capo_kafka.types.channel_status.ChannelStatus"]
    """<p>The current lifecycle state of the channel.</p>"""
    destination_type: NotRequired[
        "capo_kafka.types.channel_destination_type.ChannelDestinationType"
    ]
    """<p>The type of destination configured for the channel.</p>"""
    creation_time: NotRequired[
        "capo_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when the channel was created.</p>"""
    topic_configuration_list: NotRequired[
        "capo_kafka.types.__list_of_topic_configuration.__listOfTopicConfiguration"
    ]
    """<p>The list of topic configurations for the channel.</p>"""
    logging_info: NotRequired[
        "capo_kafka.types.channel_logging_info.ChannelLoggingInfo"
    ]
    """<p>The destinations to which the channel publishes operational logs.</p>"""
    state_info: NotRequired["capo_kafka.types.channel_state_info.ChannelStateInfo"]
    """<p>Additional context for the current channel state, populated when the channel is in FAILED.</p>"""
    cluster_operation_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the in-flight cluster operation. Returned only while the channel is in CREATING, UPDATING, or DELETING.</p>"""
    tags: NotRequired["capo_kafka.types.__map_of__string.__mapOf__string"]
    """<p>The tags attached to the channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["channelArn"] = value["channel_arn"]
    if "channel_name" in value:
        out["channelName"] = value["channel_name"]
    if "encryption_configuration" in value:
        import capo_kafka.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_kafka.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "iceberg_destination_configuration" in value:
        import capo_kafka.types.iceberg_destination_configuration

        out["icebergDestinationConfiguration"] = (
            capo_kafka.types.iceberg_destination_configuration.serialize_json(
                value["iceberg_destination_configuration"]
            )
        )
    if "s3_destination_configuration" in value:
        import capo_kafka.types.s3_destination_configuration

        out["s3DestinationConfiguration"] = (
            capo_kafka.types.s3_destination_configuration.serialize_json(
                value["s3_destination_configuration"]
            )
        )
    if "status" in value:
        import capo_kafka.types.channel_status

        out["status"] = capo_kafka.types.channel_status.serialize_json(value["status"])
    if "destination_type" in value:
        import capo_kafka.types.channel_destination_type

        out["destinationType"] = (
            capo_kafka.types.channel_destination_type.serialize_json(
                value["destination_type"]
            )
        )
    if "creation_time" in value:
        import capo_kafka.types.__timestamp_iso8601

        out["creationTime"] = capo_kafka.types.__timestamp_iso8601.serialize_json(
            value["creation_time"]
        )
    if "topic_configuration_list" in value:
        import capo_kafka.types.__list_of_topic_configuration

        out["topicConfigurationList"] = (
            capo_kafka.types.__list_of_topic_configuration.serialize_json(
                value["topic_configuration_list"]
            )
        )
    if "logging_info" in value:
        import capo_kafka.types.channel_logging_info

        out["loggingInfo"] = capo_kafka.types.channel_logging_info.serialize_json(
            value["logging_info"]
        )
    if "state_info" in value:
        import capo_kafka.types.channel_state_info

        out["stateInfo"] = capo_kafka.types.channel_state_info.serialize_json(
            value["state_info"]
        )
    if "cluster_operation_arn" in value:
        out["clusterOperationArn"] = value["cluster_operation_arn"]
    if "tags" in value:
        import capo_kafka.types.__map_of__string

        out["tags"] = capo_kafka.types.__map_of__string.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribeChannelResponse:
    out: DescribeChannelResponse = {}  # type: ignore[typeddict-item]
    if data.get("channelArn") is not None:
        out["channel_arn"] = data["channelArn"]
    if data.get("channelName") is not None:
        out["channel_name"] = data["channelName"]
    if data.get("encryptionConfiguration") is not None:
        import capo_kafka.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_kafka.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if data.get("icebergDestinationConfiguration") is not None:
        import capo_kafka.types.iceberg_destination_configuration

        out["iceberg_destination_configuration"] = (
            capo_kafka.types.iceberg_destination_configuration.deserialize_json(
                data["icebergDestinationConfiguration"]
            )
        )
    if data.get("s3DestinationConfiguration") is not None:
        import capo_kafka.types.s3_destination_configuration

        out["s3_destination_configuration"] = (
            capo_kafka.types.s3_destination_configuration.deserialize_json(
                data["s3DestinationConfiguration"]
            )
        )
    if data.get("status") is not None:
        import capo_kafka.types.channel_status

        out["status"] = capo_kafka.types.channel_status.deserialize_json(data["status"])
    if data.get("destinationType") is not None:
        import capo_kafka.types.channel_destination_type

        out["destination_type"] = (
            capo_kafka.types.channel_destination_type.deserialize_json(
                data["destinationType"]
            )
        )
    if data.get("creationTime") is not None:
        import capo_kafka.types.__timestamp_iso8601

        out["creation_time"] = capo_kafka.types.__timestamp_iso8601.deserialize_json(
            data["creationTime"]
        )
    if data.get("topicConfigurationList") is not None:
        import capo_kafka.types.__list_of_topic_configuration

        out["topic_configuration_list"] = (
            capo_kafka.types.__list_of_topic_configuration.deserialize_json(
                data["topicConfigurationList"]
            )
        )
    if data.get("loggingInfo") is not None:
        import capo_kafka.types.channel_logging_info

        out["logging_info"] = capo_kafka.types.channel_logging_info.deserialize_json(
            data["loggingInfo"]
        )
    if data.get("stateInfo") is not None:
        import capo_kafka.types.channel_state_info

        out["state_info"] = capo_kafka.types.channel_state_info.deserialize_json(
            data["stateInfo"]
        )
    if data.get("clusterOperationArn") is not None:
        out["cluster_operation_arn"] = data["clusterOperationArn"]
    if data.get("tags") is not None:
        import capo_kafka.types.__map_of__string

        out["tags"] = capo_kafka.types.__map_of__string.deserialize_json(data["tags"])
    return out
