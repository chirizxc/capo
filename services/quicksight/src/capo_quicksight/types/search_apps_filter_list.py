"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchAppsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.search_apps_filter

SearchAppsFilterList: TypeAlias = list[
    "capo_quicksight.types.search_apps_filter.SearchAppsFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchAppsFilterList) -> list:
    import capo_quicksight.types.search_apps_filter

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.search_apps_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchAppsFilterList:
    import capo_quicksight.types.search_apps_filter

    out: SearchAppsFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.search_apps_filter.deserialize_json(item))
    return out
