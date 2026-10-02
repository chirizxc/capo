"""Generated from Smithy shape ``com.amazonaws.glue#IterableFormListItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.iterable_form_list_item

IterableFormListItemList: TypeAlias = list[
    "capo_glue.types.iterable_form_list_item.IterableFormListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IterableFormListItemList) -> list:
    import capo_glue.types.iterable_form_list_item

    out: list = []
    for item in value:
        out.append(capo_glue.types.iterable_form_list_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IterableFormListItemList:
    import capo_glue.types.iterable_form_list_item

    out: IterableFormListItemList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_glue.types.iterable_form_list_item.deserialize_aws_json_1_1(item)
        )
    return out
