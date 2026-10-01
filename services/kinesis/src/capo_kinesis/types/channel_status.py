"""Generated from Smithy shape ``com.amazonaws.kinesis#ChannelStatus``."""

from typing import Literal, TypeAlias, cast

ChannelStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChannelStatus:
    return cast(ChannelStatus, data)
