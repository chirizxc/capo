"""Generated from Smithy shape ``com.amazonaws.quicksight#ApprovalGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.arn

ApprovalGroupList: TypeAlias = list["capo_quicksight.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalGroupList) -> list:
    return list(value)


def deserialize_json(data: list) -> ApprovalGroupList:
    return [item for item in data if item is not None]
