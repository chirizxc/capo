"""Generated from Smithy shape ``com.amazonaws.dynamodb#SearchSchema``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.search_schema_element

SearchSchema: TypeAlias = list[
    "capo_dynamodb.types.search_schema_element.SearchSchemaElement"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchSchema) -> list:
    import capo_dynamodb.types.search_schema_element

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.search_schema_element.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SearchSchema:
    import capo_dynamodb.types.search_schema_element

    out: SearchSchema = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.search_schema_element.deserialize_aws_json_1_0(item)
        )
    return out
