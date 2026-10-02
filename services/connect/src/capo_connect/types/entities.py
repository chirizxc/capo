"""Generated from Smithy shape ``com.amazonaws.connect#Entities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.entity

Entities: TypeAlias = list["capo_connect.types.entity.Entity"]


# --- restJson1 ser/de ---
def serialize_json(value: Entities) -> list:
    return list(value)


def deserialize_json(data: list) -> Entities:
    return [item for item in data if item is not None]
