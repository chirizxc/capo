"""Generated from Smithy shape ``com.amazonaws.kinesis#S3TablesCompressionType``."""

from typing import Literal, TypeAlias, cast

S3TablesCompressionType: TypeAlias = Literal[
    "NONE",
    "ZSTD",
    "SNAPPY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3TablesCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3TablesCompressionType:
    return cast(S3TablesCompressionType, data)
