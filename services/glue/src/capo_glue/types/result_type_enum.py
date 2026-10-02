"""Generated from Smithy shape ``com.amazonaws.glue#ResultTypeEnum``."""

from typing import Literal, TypeAlias, cast

ResultTypeEnum: TypeAlias = Literal[
    "ALL",
    "PASSED_ONLY",
    "FAILED_ONLY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResultTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResultTypeEnum:
    return cast(ResultTypeEnum, data)
