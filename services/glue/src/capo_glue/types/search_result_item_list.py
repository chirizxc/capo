"""Generated from Smithy shape ``com.amazonaws.glue#SearchResultItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.search_result_item

SearchResultItemList: TypeAlias = list[
    "capo_glue.types.search_result_item.SearchResultItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchResultItemList) -> list:
    import capo_glue.types.search_result_item

    out: list = []
    for item in value:
        out.append(capo_glue.types.search_result_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SearchResultItemList:
    import capo_glue.types.search_result_item

    out: SearchResultItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_glue.types.search_result_item.deserialize_aws_json_1_1(item))
    return out
