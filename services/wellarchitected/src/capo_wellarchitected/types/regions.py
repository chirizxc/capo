"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Regions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.region

Regions: TypeAlias = list["capo_wellarchitected.types.region.Region"]


# --- restJson1 ser/de ---
def serialize_json(value: Regions) -> list:
    return list(value)


def deserialize_json(data: list) -> Regions:
    return [item for item in data if item is not None]
