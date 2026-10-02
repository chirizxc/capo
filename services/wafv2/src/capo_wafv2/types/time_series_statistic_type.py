"""Generated from Smithy shape ``com.amazonaws.wafv2#TimeSeriesStatisticType``."""

from typing import Literal, TypeAlias, cast

TimeSeriesStatisticType: TypeAlias = Literal[
    "DATE_HISTOGRAM",
    "PAYMENT_TRAFFIC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeSeriesStatisticType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TimeSeriesStatisticType:
    return cast(TimeSeriesStatisticType, data)
