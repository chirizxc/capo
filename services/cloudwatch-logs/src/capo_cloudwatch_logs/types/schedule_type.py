"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ScheduleType``."""

from typing import Literal, TypeAlias, cast

ScheduleType: TypeAlias = Literal[
    "CUSTOMER_MANAGED",
    "AWS_MANAGED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScheduleType:
    return cast(ScheduleType, data)
