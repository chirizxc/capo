"""Generated from Smithy shape ``com.amazonaws.glue#ItemErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.item_error

ItemErrorList: TypeAlias = list["capo_glue.types.item_error.ItemError"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ItemErrorList) -> list:
    import capo_glue.types.item_error

    out: list = []
    for item in value:
        out.append(capo_glue.types.item_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ItemErrorList:
    import capo_glue.types.item_error

    out: ItemErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_glue.types.item_error.deserialize_aws_json_1_1(item))
    return out
