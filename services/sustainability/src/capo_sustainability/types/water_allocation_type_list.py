"""Generated from Smithy shape ``com.amazonaws.sustainability#WaterAllocationTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sustainability.types.water_allocation_type

WaterAllocationTypeList: TypeAlias = list[
    "capo_sustainability.types.water_allocation_type.WaterAllocationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: WaterAllocationTypeList) -> list:
    import capo_sustainability.types.water_allocation_type

    out: list = []
    for item in value:
        out.append(capo_sustainability.types.water_allocation_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> WaterAllocationTypeList:
    import capo_sustainability.types.water_allocation_type

    out: WaterAllocationTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sustainability.types.water_allocation_type.deserialize_json(item)
        )
    return out
