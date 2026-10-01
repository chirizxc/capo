"""Generated from Smithy shape ``com.amazonaws.kinesis#ChannelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.channel_arn
    import capo_kinesis.types.channel_destination_type
    import capo_kinesis.types.channel_id
    import capo_kinesis.types.channel_name
    import capo_kinesis.types.channel_status
    import capo_kinesis.types.channel_status_reason
    import capo_kinesis.types.channel_stream_identifier_list
    import capo_kinesis.types.timestamp


class ChannelSummary(TypedDict, closed=True):
    channel_name: "capo_kinesis.types.channel_name.ChannelName"
    """<p>The name of the channel.</p>"""
    channel_arn: "capo_kinesis.types.channel_arn.ChannelARN"
    """<p>The Amazon Resource Name (ARN) of the channel.</p>"""
    channel_id: "capo_kinesis.types.channel_id.ChannelId"
    """<p>The unique identifier of the channel.</p>"""
    channel_status: "capo_kinesis.types.channel_status.ChannelStatus"
    """<p>The current status of the channel. Valid values:</p> <ul> <li> <p> <code>CREATING</code> - The channel is being created.</p> </li> <li> <p> <code>ACTIVE</code> - The channel is ready to deliver records.</p> </li> <li> <p> <code>UPDATING</code> - The channel configuration is being updated.</p> </li> <li> <p> <code>DELETING</code> - The channel is being deleted.</p> </li> <li> <p> <code>FAILED</code> - See <code>ChannelStatusReason</code> for the failure cause.</p> </li> </ul>"""
    channel_status_reason: NotRequired[
        "capo_kinesis.types.channel_status_reason.ChannelStatusReason"
    ]
    """<p>A message describing the reason for a <code>FAILED</code> status.</p>"""
    channel_creation_timestamp: "capo_kinesis.types.timestamp.Timestamp"
    """<p>The time at which the channel was created.</p>"""
    channel_destination_type: (
        "capo_kinesis.types.channel_destination_type.ChannelDestinationType"
    )
    """<p>The destination type of the channel. Valid values:</p> <ul> <li> <p> <code>S3</code> - Delivery to a general purpose Amazon S3 bucket.</p> </li> <li> <p> <code>S3_TABLES</code> - Delivery to streaming tables on Apache Iceberg.</p> </li> </ul>"""
    streams: (
        "capo_kinesis.types.channel_stream_identifier_list.ChannelStreamIdentifierList"
    )
    """<p>The source streams associated with the channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelSummary) -> dict:
    out: dict = {}
    out["ChannelName"] = value["channel_name"]
    out["ChannelARN"] = value["channel_arn"]
    out["ChannelId"] = value["channel_id"]
    import capo_kinesis.types.channel_status

    out["ChannelStatus"] = capo_kinesis.types.channel_status.serialize_aws_json_1_1(
        value["channel_status"]
    )
    if "channel_status_reason" in value:
        out["ChannelStatusReason"] = value["channel_status_reason"]
    import capo_kinesis.types.timestamp

    out["ChannelCreationTimestamp"] = (
        capo_kinesis.types.timestamp.serialize_aws_json_1_1(
            value["channel_creation_timestamp"]
        )
    )
    import capo_kinesis.types.channel_destination_type

    out["ChannelDestinationType"] = (
        capo_kinesis.types.channel_destination_type.serialize_aws_json_1_1(
            value["channel_destination_type"]
        )
    )
    import capo_kinesis.types.channel_stream_identifier_list

    out["Streams"] = (
        capo_kinesis.types.channel_stream_identifier_list.serialize_aws_json_1_1(
            value["streams"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ChannelSummary:
    out: ChannelSummary = {}  # type: ignore[typeddict-item]
    if data.get("ChannelName") is not None:
        out["channel_name"] = data["ChannelName"]
    else:
        raise DeserializationError("ChannelSummary.channel_name required")
    if data.get("ChannelARN") is not None:
        out["channel_arn"] = data["ChannelARN"]
    else:
        raise DeserializationError("ChannelSummary.channel_arn required")
    if data.get("ChannelId") is not None:
        out["channel_id"] = data["ChannelId"]
    else:
        raise DeserializationError("ChannelSummary.channel_id required")
    if data.get("ChannelStatus") is not None:
        import capo_kinesis.types.channel_status

        out["channel_status"] = (
            capo_kinesis.types.channel_status.deserialize_aws_json_1_1(
                data["ChannelStatus"]
            )
        )
    else:
        raise DeserializationError("ChannelSummary.channel_status required")
    if data.get("ChannelStatusReason") is not None:
        out["channel_status_reason"] = data["ChannelStatusReason"]
    if data.get("ChannelCreationTimestamp") is not None:
        import capo_kinesis.types.timestamp

        out["channel_creation_timestamp"] = (
            capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
                data["ChannelCreationTimestamp"]
            )
        )
    else:
        raise DeserializationError("ChannelSummary.channel_creation_timestamp required")
    if data.get("ChannelDestinationType") is not None:
        import capo_kinesis.types.channel_destination_type

        out["channel_destination_type"] = (
            capo_kinesis.types.channel_destination_type.deserialize_aws_json_1_1(
                data["ChannelDestinationType"]
            )
        )
    else:
        raise DeserializationError("ChannelSummary.channel_destination_type required")
    if data.get("Streams") is not None:
        import capo_kinesis.types.channel_stream_identifier_list

        out["streams"] = (
            capo_kinesis.types.channel_stream_identifier_list.deserialize_aws_json_1_1(
                data["Streams"]
            )
        )
    else:
        raise DeserializationError("ChannelSummary.streams required")
    return out
