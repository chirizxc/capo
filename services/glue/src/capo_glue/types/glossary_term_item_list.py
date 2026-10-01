"""Generated from Smithy shape ``com.amazonaws.glue#GlossaryTermItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.glossary_term_item

GlossaryTermItemList: TypeAlias = list[
    "capo_glue.types.glossary_term_item.GlossaryTermItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlossaryTermItemList) -> list:
    import capo_glue.types.glossary_term_item

    out: list = []
    for item in value:
        out.append(capo_glue.types.glossary_term_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GlossaryTermItemList:
    import capo_glue.types.glossary_term_item

    out: GlossaryTermItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_glue.types.glossary_term_item.deserialize_aws_json_1_1(item))
    return out
