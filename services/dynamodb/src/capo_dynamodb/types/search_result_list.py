"""Generated from Smithy shape ``com.amazonaws.dynamodb#SearchResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.search_result_item

SearchResultList: TypeAlias = list[
    "capo_dynamodb.types.search_result_item.SearchResultItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchResultList) -> list:
    import capo_dynamodb.types.search_result_item

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.search_result_item.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> SearchResultList:
    import capo_dynamodb.types.search_result_item

    out: SearchResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.search_result_item.deserialize_aws_json_1_0(item)
        )
    return out
