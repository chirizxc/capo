"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GoalIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.uuid

GoalIdList: TypeAlias = list["capo_wellarchitected.types.uuid.UUID"]


# --- restJson1 ser/de ---
def serialize_json(value: GoalIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> GoalIdList:
    return [item for item in data if item is not None]
