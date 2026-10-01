"""Generated from Smithy shape ``com.amazonaws.kinesis#S3CompressionType``."""

from typing import Literal, TypeAlias, cast

S3CompressionType: TypeAlias = Literal[
    "NONE",
    "GZIP",
    "ZSTD",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3CompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3CompressionType:
    return cast(S3CompressionType, data)
