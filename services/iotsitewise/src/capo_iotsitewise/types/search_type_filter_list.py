"""Generated from Smithy shape ``com.amazonaws.iotsitewise#SearchTypeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.search_type

SearchTypeFilterList: TypeAlias = list["capo_iotsitewise.types.search_type.SearchType"]


# --- restJson1 ser/de ---
def serialize_json(value: SearchTypeFilterList) -> list:
    import capo_iotsitewise.types.search_type

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.search_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchTypeFilterList:
    import capo_iotsitewise.types.search_type

    out: SearchTypeFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iotsitewise.types.search_type.deserialize_json(item))
    return out
