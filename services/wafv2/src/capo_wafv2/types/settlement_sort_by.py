"""Generated from Smithy shape ``com.amazonaws.wafv2#SettlementSortBy``."""

from typing import Literal, TypeAlias, cast

SettlementSortBy: TypeAlias = Literal[
    "TIMESTAMP",
    "AMOUNT",
    "NAME",
    "STATUS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SettlementSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SettlementSortBy:
    return cast(SettlementSortBy, data)
