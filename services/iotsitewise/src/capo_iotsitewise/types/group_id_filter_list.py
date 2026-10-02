"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GroupIdFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.group_id

GroupIdFilterList: TypeAlias = list["capo_iotsitewise.types.group_id.GroupId"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupIdFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> GroupIdFilterList:
    return [item for item in data if item is not None]
