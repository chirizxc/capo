"""Generated from Smithy shape ``com.amazonaws.glue#SearchSortOrder``."""

from typing import Literal, TypeAlias, cast

SearchSortOrder: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SearchSortOrder:
    return cast(SearchSortOrder, data)
