"""Generated from Smithy shape ``com.amazonaws.sustainability#WaterAllocationType``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the types of water allocation calculations available.</p>"""
WaterAllocationType: TypeAlias = Literal["TOTAL_WATER_WITHDRAWALS",]


# --- restJson1 ser/de ---
def serialize_json(value: WaterAllocationType) -> str:
    return value


def deserialize_json(data: str) -> WaterAllocationType:
    return cast(WaterAllocationType, data)
