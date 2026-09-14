"""Generated from Smithy shape ``com.amazonaws.geoplaces#BoundingBox``."""

from typing import TypeAlias

BoundingBox: TypeAlias = list["float"]


# --- restJson1 ser/de ---
def serialize_json(value: BoundingBox) -> list:
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


def deserialize_json(data: list) -> BoundingBox:
    return [float(item) for item in data if item is not None]
