"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SyslogSourceType``."""

from typing import Literal, TypeAlias, cast

SyslogSourceType: TypeAlias = Literal["VPCE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SyslogSourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SyslogSourceType:
    return cast(SyslogSourceType, data)
