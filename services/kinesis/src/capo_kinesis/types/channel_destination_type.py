"""Generated from Smithy shape ``com.amazonaws.kinesis#ChannelDestinationType``."""

from typing import Literal, TypeAlias, cast

ChannelDestinationType: TypeAlias = Literal[
    "S3",
    "S3_TABLES",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelDestinationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChannelDestinationType:
    return cast(ChannelDestinationType, data)
