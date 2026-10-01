"""Generated from Smithy shape ``com.amazonaws.iotsitewise#SearchResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.search_result

SearchResultList: TypeAlias = list["capo_iotsitewise.types.search_result.SearchResult"]


# --- restJson1 ser/de ---
def serialize_json(value: SearchResultList) -> list:
    import capo_iotsitewise.types.search_result

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.search_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchResultList:
    import capo_iotsitewise.types.search_result

    out: SearchResultList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iotsitewise.types.search_result.deserialize_json(item))
    return out
