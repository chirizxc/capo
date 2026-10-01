"""Generated from Smithy shape ``com.amazonaws.sustainability#DimensionValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sustainability.types.dimension_value

DimensionValueList: TypeAlias = list[
    "capo_sustainability.types.dimension_value.DimensionValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> DimensionValueList:
    return [item for item in data if item is not None]
