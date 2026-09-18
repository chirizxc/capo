"""Generated from Smithy shape ``com.amazonaws.location#Position``."""

from typing import TypeAlias

Position: TypeAlias = list["float"]


# --- restJson1 ser/de ---
def serialize_json(value: Position) -> list:
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


def deserialize_json(data: list) -> Position:
    return [float(item) for item in data if item is not None]
