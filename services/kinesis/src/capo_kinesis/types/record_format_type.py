"""Generated from Smithy shape ``com.amazonaws.kinesis#RecordFormatType``."""

from typing import Literal, TypeAlias, cast

RecordFormatType: TypeAlias = Literal[
    "GSR_JSON",
    "JSON",
    "STRING",
    "BYTE_ARRAY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordFormatType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordFormatType:
    return cast(RecordFormatType, data)
