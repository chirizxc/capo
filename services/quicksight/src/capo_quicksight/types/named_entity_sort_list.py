"""Generated from Smithy shape ``com.amazonaws.quicksight#NamedEntitySortList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.named_entity_sort

NamedEntitySortList: TypeAlias = list[
    "capo_quicksight.types.named_entity_sort.NamedEntitySort"
]


# --- restJson1 ser/de ---
def serialize_json(value: NamedEntitySortList) -> list:
    import capo_quicksight.types.named_entity_sort

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.named_entity_sort.serialize_json(item))
    return out


def deserialize_json(data: list) -> NamedEntitySortList:
    import capo_quicksight.types.named_entity_sort

    out: NamedEntitySortList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.named_entity_sort.deserialize_json(item))
    return out
