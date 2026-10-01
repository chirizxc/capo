"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Highlights``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.highlight

Highlights: TypeAlias = list["capo_wellarchitected.types.highlight.Highlight"]


# --- restJson1 ser/de ---
def serialize_json(value: Highlights) -> list:
    return list(value)


def deserialize_json(data: list) -> Highlights:
    return [item for item in data if item is not None]
