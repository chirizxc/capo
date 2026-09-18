"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionCoordinate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.position_coordinate_value

PositionCoordinate: TypeAlias = list[
    "capo_iot_wireless.types.position_coordinate_value.PositionCoordinateValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: PositionCoordinate) -> list:
    return [
        (
            "NaN"
            if item != item
            else "Infinity"
            if item == float("inf")
            else "-Infinity"
            if item == float("-inf")
            else item
        )
        for item in value
    ]


def deserialize_json(data: list) -> PositionCoordinate:
    return [float(item) for item in data if item is not None]
