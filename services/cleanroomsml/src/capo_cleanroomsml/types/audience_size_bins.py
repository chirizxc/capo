"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceSizeBins``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.audience_size_value

AudienceSizeBins: TypeAlias = list[
    "capo_cleanroomsml.types.audience_size_value.AudienceSizeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AudienceSizeBins) -> list:
    return list(value)


def deserialize_json(data: list) -> AudienceSizeBins:
    return [item for item in data if item is not None]
