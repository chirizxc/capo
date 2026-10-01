"""Generated from Smithy shape ``com.amazonaws.kafka#CreateChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__list_of_topic_configuration
    import capo_kafka.types.__map_of__string
    import capo_kafka.types.__string
    import capo_kafka.types.channel_logging_info
    import capo_kafka.types.encryption_configuration
    import capo_kafka.types.iceberg_destination_configuration
    import capo_kafka.types.s3_destination_configuration


class CreateChannelRequest(TypedDict, closed=True):
    channel_name: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The name of the channel. Must be unique within the cluster.</p>"""
    cluster_arn: "capo_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    encryption_configuration: NotRequired[
        "capo_kafka.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration applied to the channel.</p>"""
    iceberg_destination_configuration: NotRequired[
        "capo_kafka.types.iceberg_destination_configuration.IcebergDestinationConfiguration"
    ]
    """<p>The Apache Iceberg destination for the channel. Mutually exclusive with s3DestinationConfiguration.</p>"""
    s3_destination_configuration: NotRequired[
        "capo_kafka.types.s3_destination_configuration.S3DestinationConfiguration"
    ]
    """<p>The Amazon S3 destination for the channel. Mutually exclusive with icebergDestinationConfiguration.</p>"""
    tags: NotRequired["capo_kafka.types.__map_of__string.__mapOf__string"]
    """<p>The tags attached to the channel.</p>"""
    topic_configuration_list: NotRequired[
        "capo_kafka.types.__list_of_topic_configuration.__listOfTopicConfiguration"
    ]
    """<p>The list of topic configurations for the channel. Currently exactly one topic must be specified.</p>"""
    logging_info: NotRequired[
        "capo_kafka.types.channel_logging_info.ChannelLoggingInfo"
    ]
    """<p>The destinations to which the channel publishes operational logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelRequest) -> dict:
    out: dict = {}
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
    if "tags" in value:
        import capo_kafka.types.__map_of__string

        out["tags"] = capo_kafka.types.__map_of__string.serialize_json(value["tags"])
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
    return out


def deserialize_json(data: dict) -> CreateChannelRequest:
    out: CreateChannelRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("tags") is not None:
        import capo_kafka.types.__map_of__string

        out["tags"] = capo_kafka.types.__map_of__string.deserialize_json(data["tags"])
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
    return out
