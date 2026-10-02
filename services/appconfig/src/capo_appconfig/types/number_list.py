"""Generated from Smithy shape ``com.amazonaws.appconfig#NumberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.double

NumberList: TypeAlias = list["capo_appconfig.types.double.Double"]


# --- restJson1 ser/de ---
def serialize_json(value: NumberList) -> list:
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


def deserialize_json(data: list) -> NumberList:
    return [float(item) for item in data if item is not None]
