"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ColumnLineageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.column_lineage_entry

ColumnLineageList: TypeAlias = list[
    "capo_cleanrooms.types.column_lineage_entry.ColumnLineageEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnLineageList) -> list:
    import capo_cleanrooms.types.column_lineage_entry

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.column_lineage_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnLineageList:
    import capo_cleanrooms.types.column_lineage_entry

    out: ColumnLineageList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cleanrooms.types.column_lineage_entry.deserialize_json(item))
    return out
