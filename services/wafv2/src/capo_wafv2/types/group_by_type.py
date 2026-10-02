"""Generated from Smithy shape ``com.amazonaws.wafv2#GroupByType``."""

from typing import Literal, TypeAlias, cast

GroupByType: TypeAlias = Literal[
    "NAME",
    "CATEGORY",
    "INTENT",
    "ORGANIZATION",
    "WEBACL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupByType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GroupByType:
    return cast(GroupByType, data)
