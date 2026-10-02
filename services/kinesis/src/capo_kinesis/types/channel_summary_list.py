"""Generated from Smithy shape ``com.amazonaws.kinesis#ChannelSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.channel_summary

ChannelSummaryList: TypeAlias = list[
    "capo_kinesis.types.channel_summary.ChannelSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelSummaryList) -> list:
    import capo_kinesis.types.channel_summary

    out: list = []
    for item in value:
        out.append(capo_kinesis.types.channel_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ChannelSummaryList:
    import capo_kinesis.types.channel_summary

    out: ChannelSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_kinesis.types.channel_summary.deserialize_aws_json_1_1(item))
    return out
