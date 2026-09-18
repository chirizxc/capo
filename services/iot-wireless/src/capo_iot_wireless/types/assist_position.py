"""Generated from Smithy shape ``com.amazonaws.iotwireless#AssistPosition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.coordinate

AssistPosition: TypeAlias = list["capo_iot_wireless.types.coordinate.Coordinate"]


# --- restJson1 ser/de ---
def serialize_json(value: AssistPosition) -> list:
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


def deserialize_json(data: list) -> AssistPosition:
    return [float(item) for item in data if item is not None]
