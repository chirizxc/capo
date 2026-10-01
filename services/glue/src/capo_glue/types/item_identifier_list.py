"""Generated from Smithy shape ``com.amazonaws.glue#ItemIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.item_identifier

ItemIdentifierList: TypeAlias = list["capo_glue.types.item_identifier.ItemIdentifier"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ItemIdentifierList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ItemIdentifierList:
    return [item for item in data if item is not None]
