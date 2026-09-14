"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOf__doubleMinNegative60Max6``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.__double_min_negative60_max6

__listOf__doubleMinNegative60Max6: TypeAlias = list[
    "capo_mediaconvert.types.__double_min_negative60_max6.__doubleMinNegative60Max6"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__doubleMinNegative60Max6) -> list:
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


def deserialize_json(data: list) -> __listOf__doubleMinNegative60Max6:
    return [float(item) for item in data if item is not None]
