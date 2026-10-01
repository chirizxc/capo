"""Generated from Smithy shape ``com.amazonaws.sustainability#WaterAllocationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sustainability.types.water_allocation
    import capo_sustainability.types.water_allocation_type

WaterAllocationMap: TypeAlias = dict[
    "capo_sustainability.types.water_allocation_type.WaterAllocationType",
    "capo_sustainability.types.water_allocation.WaterAllocation",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: WaterAllocationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sustainability.types.water_allocation
        import capo_sustainability.types.water_allocation_type

        out[capo_sustainability.types.water_allocation_type.serialize_json(key)] = (
            capo_sustainability.types.water_allocation.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> WaterAllocationMap:
    out: WaterAllocationMap = {}
    for key, value in data.items():
        import capo_sustainability.types.water_allocation_type

        if value is None:
            continue
        import capo_sustainability.types.water_allocation

        out[capo_sustainability.types.water_allocation_type.deserialize_json(key)] = (
            capo_sustainability.types.water_allocation.deserialize_json(value)
        )
    return out
