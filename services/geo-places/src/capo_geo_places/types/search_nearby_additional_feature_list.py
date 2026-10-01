"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchNearbyAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.search_nearby_additional_feature

SearchNearbyAdditionalFeatureList: TypeAlias = list[
    "capo_geo_places.types.search_nearby_additional_feature.SearchNearbyAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchNearbyAdditionalFeatureList) -> list:
    import capo_geo_places.types.search_nearby_additional_feature

    out: list = []
    for item in value:
        out.append(
            capo_geo_places.types.search_nearby_additional_feature.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchNearbyAdditionalFeatureList:
    import capo_geo_places.types.search_nearby_additional_feature

    out: SearchNearbyAdditionalFeatureList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_places.types.search_nearby_additional_feature.deserialize_json(
                item
            )
        )
    return out
