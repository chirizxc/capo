"""Generated from Smithy shape ``com.amazonaws.kinesis#ChannelEncryptionType``."""

from typing import Literal, TypeAlias, cast

ChannelEncryptionType: TypeAlias = Literal["KMS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelEncryptionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChannelEncryptionType:
    return cast(ChannelEncryptionType, data)
