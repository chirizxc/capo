"""Generated from Smithy shape ``com.amazonaws.quicksight#LinkedDataSourceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.linked_data_source_id

LinkedDataSourceIds: TypeAlias = list[
    "capo_quicksight.types.linked_data_source_id.LinkedDataSourceId"
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkedDataSourceIds) -> list:
    return list(value)


def deserialize_json(data: list) -> LinkedDataSourceIds:
    return [item for item in data if item is not None]
