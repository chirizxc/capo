"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteFilterPlaceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.autocomplete_filter_place_type

AutocompleteFilterPlaceTypeList: TypeAlias = list[
    "capo_geo_places.types.autocomplete_filter_place_type.AutocompleteFilterPlaceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteFilterPlaceTypeList) -> list:
    import capo_geo_places.types.autocomplete_filter_place_type

    out: list = []
    for item in value:
        out.append(
            capo_geo_places.types.autocomplete_filter_place_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutocompleteFilterPlaceTypeList:
    import capo_geo_places.types.autocomplete_filter_place_type

    out: AutocompleteFilterPlaceTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_places.types.autocomplete_filter_place_type.deserialize_json(item)
        )
    return out
