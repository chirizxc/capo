"""Generated from Smithy shape ``com.amazonaws.glue#GlossaryTermIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.glossary_term_id

GlossaryTermIdList: TypeAlias = list["capo_glue.types.glossary_term_id.GlossaryTermId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlossaryTermIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> GlossaryTermIdList:
    return [item for item in data if item is not None]
