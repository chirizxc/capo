"""Generated from Smithy shape ``com.amazonaws.connect#SupportedStatsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.string

SupportedStatsList: TypeAlias = list["capo_connect.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedStatsList) -> list:
    return list(value)


def deserialize_json(data: list) -> SupportedStatsList:
    return [item for item in data if item is not None]
