"""Generated from Smithy shape ``com.amazonaws.kafka#__listOf__double``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.__double

__listOf__double: TypeAlias = list["capo_kafka.types.__double.__double"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__double) -> list:
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


def deserialize_json(data: list) -> __listOf__double:
    return [float(item) for item in data if item is not None]
