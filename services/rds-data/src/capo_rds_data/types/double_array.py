"""Generated from Smithy shape ``com.amazonaws.rdsdata#DoubleArray``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rds_data.types.boxed_double

DoubleArray: TypeAlias = list["capo_rds_data.types.boxed_double.BoxedDouble | None"]


# --- restJson1 ser/de ---
def serialize_json(value: DoubleArray) -> list:
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


def deserialize_json(data: list) -> DoubleArray:
    return [None if item is None else float(item) for item in data]
