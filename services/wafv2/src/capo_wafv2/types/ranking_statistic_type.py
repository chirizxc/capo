"""Generated from Smithy shape ``com.amazonaws.wafv2#RankingStatisticType``."""

from typing import Literal, TypeAlias, cast

RankingStatisticType: TypeAlias = Literal[
    "TOP_SOURCES_BY_REVENUE",
    "TOP_PATHS_BY_REVENUE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RankingStatisticType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RankingStatisticType:
    return cast(RankingStatisticType, data)
