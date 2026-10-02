"""Generated from Smithy shape ``com.amazonaws.connect#AvailableFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.available_filter

AvailableFilterList: TypeAlias = list[
    "capo_connect.types.available_filter.AvailableFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AvailableFilterList) -> list:
    import capo_connect.types.available_filter

    out: list = []
    for item in value:
        out.append(capo_connect.types.available_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> AvailableFilterList:
    import capo_connect.types.available_filter

    out: AvailableFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.available_filter.deserialize_json(item))
    return out
