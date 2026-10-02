"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicV2DataSetRelationColumnNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.string

TopicV2DataSetRelationColumnNames: TypeAlias = list[
    "capo_quicksight.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicV2DataSetRelationColumnNames) -> list:
    return list(value)


def deserialize_json(data: list) -> TopicV2DataSetRelationColumnNames:
    return [item for item in data if item is not None]
