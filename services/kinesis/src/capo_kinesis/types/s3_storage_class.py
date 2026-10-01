"""Generated from Smithy shape ``com.amazonaws.kinesis#S3StorageClass``."""

from typing import Literal, TypeAlias, cast

S3StorageClass: TypeAlias = Literal[
    "STANDARD",
    "INTELLIGENT_TIERING",
    "GLACIER_IR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3StorageClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3StorageClass:
    return cast(S3StorageClass, data)
