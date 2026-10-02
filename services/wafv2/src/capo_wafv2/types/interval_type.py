"""Generated from Smithy shape ``com.amazonaws.wafv2#IntervalType``."""

from typing import Literal, TypeAlias, cast

IntervalType: TypeAlias = Literal[
    "MINUTELY",
    "FIVE_MINUTELY",
    "HOURLY",
    "DAILY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntervalType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IntervalType:
    return cast(IntervalType, data)
