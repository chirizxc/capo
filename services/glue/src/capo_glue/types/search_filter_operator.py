"""Generated from Smithy shape ``com.amazonaws.glue#SearchFilterOperator``."""

from typing import Literal, TypeAlias, cast

SearchFilterOperator: TypeAlias = Literal[
    "equals",
    "greaterThan",
    "greaterThanOrEquals",
    "lessThan",
    "lessThanOrEquals",
    "notExists",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchFilterOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SearchFilterOperator:
    return cast(SearchFilterOperator, data)
