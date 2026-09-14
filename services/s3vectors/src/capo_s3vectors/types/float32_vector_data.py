"""Generated from Smithy shape ``com.amazonaws.s3vectors#Float32VectorData``."""

from typing import TypeAlias

Float32VectorData: TypeAlias = list["float"]


# --- restJson1 ser/de ---
def serialize_json(value: Float32VectorData) -> list:
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


def deserialize_json(data: list) -> Float32VectorData:
    return [float(item) for item in data if item is not None]
