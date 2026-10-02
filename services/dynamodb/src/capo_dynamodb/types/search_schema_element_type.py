"""Generated from Smithy shape ``com.amazonaws.dynamodb#SearchSchemaElementType``."""

from typing import Literal, TypeAlias, cast

SearchSchemaElementType: TypeAlias = Literal[
    "HASH",
    "INLINE_FILTER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchSchemaElementType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SearchSchemaElementType:
    return cast(SearchSchemaElementType, data)
