"""Generated from Smithy shape ``com.amazonaws.sustainability#WaterAllocationUnit``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the unit of measurement for allocation.</p>"""
WaterAllocationUnit: TypeAlias = Literal["m3",]


# --- restJson1 ser/de ---
def serialize_json(value: WaterAllocationUnit) -> str:
    return value


def deserialize_json(data: str) -> WaterAllocationUnit:
    return cast(WaterAllocationUnit, data)
