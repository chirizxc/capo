"""Generated from Smithy shape ``com.amazonaws.glue#IterableFormItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.iterable_form_item

IterableFormItemList: TypeAlias = list[
    "capo_glue.types.iterable_form_item.IterableFormItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IterableFormItemList) -> list:
    import capo_glue.types.iterable_form_item

    out: list = []
    for item in value:
        out.append(capo_glue.types.iterable_form_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IterableFormItemList:
    import capo_glue.types.iterable_form_item

    out: IterableFormItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_glue.types.iterable_form_item.deserialize_aws_json_1_1(item))
    return out
