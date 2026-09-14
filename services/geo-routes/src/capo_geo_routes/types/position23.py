"""Generated from Smithy shape ``com.amazonaws.georoutes#Position23``."""

from typing import TypeAlias

Position23: TypeAlias = list["float"]


# --- restJson1 ser/de ---
def serialize_json(value: Position23) -> list:
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


def deserialize_json(data: list) -> Position23:
    return [float(item) for item in data if item is not None]
