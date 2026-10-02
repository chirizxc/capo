"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table_column

IntermediateTableColumnList: TypeAlias = list[
    "capo_cleanrooms.types.intermediate_table_column.IntermediateTableColumn"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableColumnList) -> list:
    import capo_cleanrooms.types.intermediate_table_column

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.intermediate_table_column.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntermediateTableColumnList:
    import capo_cleanrooms.types.intermediate_table_column

    out: IntermediateTableColumnList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cleanrooms.types.intermediate_table_column.deserialize_json(item)
        )
    return out
