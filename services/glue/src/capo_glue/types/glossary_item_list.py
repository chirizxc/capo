"""Generated from Smithy shape ``com.amazonaws.glue#GlossaryItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.glossary_item

GlossaryItemList: TypeAlias = list["capo_glue.types.glossary_item.GlossaryItem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlossaryItemList) -> list:
    import capo_glue.types.glossary_item

    out: list = []
    for item in value:
        out.append(capo_glue.types.glossary_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GlossaryItemList:
    import capo_glue.types.glossary_item

    out: GlossaryItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_glue.types.glossary_item.deserialize_aws_json_1_1(item))
    return out
