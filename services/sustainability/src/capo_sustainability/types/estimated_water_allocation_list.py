"""Generated from Smithy shape ``com.amazonaws.sustainability#EstimatedWaterAllocationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sustainability.types.estimated_water_allocation

EstimatedWaterAllocationList: TypeAlias = list[
    "capo_sustainability.types.estimated_water_allocation.EstimatedWaterAllocation"
]


# --- restJson1 ser/de ---
def serialize_json(value: EstimatedWaterAllocationList) -> list:
    import capo_sustainability.types.estimated_water_allocation

    out: list = []
    for item in value:
        out.append(
            capo_sustainability.types.estimated_water_allocation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EstimatedWaterAllocationList:
    import capo_sustainability.types.estimated_water_allocation

    out: EstimatedWaterAllocationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sustainability.types.estimated_water_allocation.deserialize_json(item)
        )
    return out
