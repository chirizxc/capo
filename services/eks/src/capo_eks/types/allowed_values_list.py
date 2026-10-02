"""Generated from Smithy shape ``com.amazonaws.eks#AllowedValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.string

AllowedValuesList: TypeAlias = list["capo_eks.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedValuesList) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedValuesList:
    return [item for item in data if item is not None]
