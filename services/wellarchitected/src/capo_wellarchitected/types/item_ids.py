"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ItemIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.item_id

ItemIds: TypeAlias = list["capo_wellarchitected.types.item_id.ItemId"]


# --- restJson1 ser/de ---
def serialize_json(value: ItemIds) -> list:
    return list(value)


def deserialize_json(data: list) -> ItemIds:
    return [item for item in data if item is not None]
