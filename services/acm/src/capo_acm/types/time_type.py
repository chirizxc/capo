"""Generated from Smithy shape ``com.amazonaws.acm#TimeType``."""

from typing import Literal, TypeAlias, cast

TimeType: TypeAlias = Literal[
    "MINUTES",
    "HOURS",
    "DAYS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TimeType:
    return cast(TimeType, data)
