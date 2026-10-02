"""Generated from Smithy shape ``com.amazonaws.geoplaces#GetPlaceAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.get_place_additional_feature

GetPlaceAdditionalFeatureList: TypeAlias = list[
    "capo_geo_places.types.get_place_additional_feature.GetPlaceAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaceAdditionalFeatureList) -> list:
    import capo_geo_places.types.get_place_additional_feature

    out: list = []
    for item in value:
        out.append(
            capo_geo_places.types.get_place_additional_feature.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GetPlaceAdditionalFeatureList:
    import capo_geo_places.types.get_place_additional_feature

    out: GetPlaceAdditionalFeatureList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_places.types.get_place_additional_feature.deserialize_json(item)
        )
    return out
