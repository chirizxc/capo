"""Generated from Smithy shape ``com.amazonaws.glue#FormTypeItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.form_type_item

FormTypeItemList: TypeAlias = list["capo_glue.types.form_type_item.FormTypeItem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FormTypeItemList) -> list:
    import capo_glue.types.form_type_item

    out: list = []
    for item in value:
        out.append(capo_glue.types.form_type_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FormTypeItemList:
    import capo_glue.types.form_type_item

    out: FormTypeItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_glue.types.form_type_item.deserialize_aws_json_1_1(item))
    return out
