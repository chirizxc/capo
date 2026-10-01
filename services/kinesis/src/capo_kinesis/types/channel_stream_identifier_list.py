"""Generated from Smithy shape ``com.amazonaws.kinesis#ChannelStreamIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.channel_stream_identifier

ChannelStreamIdentifierList: TypeAlias = list[
    "capo_kinesis.types.channel_stream_identifier.ChannelStreamIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelStreamIdentifierList) -> list:
    import capo_kinesis.types.channel_stream_identifier

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.channel_stream_identifier.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ChannelStreamIdentifierList:
    import capo_kinesis.types.channel_stream_identifier

    out: ChannelStreamIdentifierList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.channel_stream_identifier.deserialize_aws_json_1_1(item)
        )
    return out
