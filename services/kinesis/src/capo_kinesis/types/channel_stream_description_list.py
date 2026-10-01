"""Generated from Smithy shape ``com.amazonaws.kinesis#ChannelStreamDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.channel_stream_description

ChannelStreamDescriptionList: TypeAlias = list[
    "capo_kinesis.types.channel_stream_description.ChannelStreamDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelStreamDescriptionList) -> list:
    import capo_kinesis.types.channel_stream_description

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.channel_stream_description.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ChannelStreamDescriptionList:
    import capo_kinesis.types.channel_stream_description

    out: ChannelStreamDescriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.channel_stream_description.deserialize_aws_json_1_1(item)
        )
    return out
