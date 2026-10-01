"""Generated from Smithy shape ``com.amazonaws.iotsitewise#SearchStatusFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.search_status

SearchStatusFilterList: TypeAlias = list[
    "capo_iotsitewise.types.search_status.SearchStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchStatusFilterList) -> list:
    import capo_iotsitewise.types.search_status

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.search_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchStatusFilterList:
    import capo_iotsitewise.types.search_status

    out: SearchStatusFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iotsitewise.types.search_status.deserialize_json(item))
    return out
