"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#IndexCategory``."""

from typing import Literal, TypeAlias, cast

IndexCategory: TypeAlias = Literal[
    "DEFAULT",
    "CUSTOM",
    "AUTO",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IndexCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IndexCategory:
    return cast(IndexCategory, data)
