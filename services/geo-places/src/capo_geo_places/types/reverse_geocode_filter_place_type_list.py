"""Generated from Smithy shape ``com.amazonaws.geoplaces#ReverseGeocodeFilterPlaceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.reverse_geocode_filter_place_type

ReverseGeocodeFilterPlaceTypeList: TypeAlias = list[
    "capo_geo_places.types.reverse_geocode_filter_place_type.ReverseGeocodeFilterPlaceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReverseGeocodeFilterPlaceTypeList) -> list:
    import capo_geo_places.types.reverse_geocode_filter_place_type

    out: list = []
    for item in value:
        out.append(
            capo_geo_places.types.reverse_geocode_filter_place_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReverseGeocodeFilterPlaceTypeList:
    import capo_geo_places.types.reverse_geocode_filter_place_type

    out: ReverseGeocodeFilterPlaceTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_places.types.reverse_geocode_filter_place_type.deserialize_json(
                item
            )
        )
    return out
