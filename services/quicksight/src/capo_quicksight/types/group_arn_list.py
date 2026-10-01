"""Generated from Smithy shape ``com.amazonaws.quicksight#GroupArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.arn

GroupArnList: TypeAlias = list["capo_quicksight.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> GroupArnList:
    return [item for item in data if item is not None]
