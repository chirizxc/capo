"""Generated from Smithy shape ``com.amazonaws.connect#NumberValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.double

NumberValueList: TypeAlias = list["capo_connect.types.double.Double"]


# --- restJson1 ser/de ---
def serialize_json(value: NumberValueList) -> list:
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


def deserialize_json(data: list) -> NumberValueList:
    return [float(item) for item in data if item is not None]
