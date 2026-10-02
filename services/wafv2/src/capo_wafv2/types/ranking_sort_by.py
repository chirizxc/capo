"""Generated from Smithy shape ``com.amazonaws.wafv2#RankingSortBy``."""

from typing import Literal, TypeAlias, cast

RankingSortBy: TypeAlias = Literal[
    "REVENUE",
    "PERCENTAGE",
    "NAME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RankingSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RankingSortBy:
    return cast(RankingSortBy, data)
