"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchTextAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.search_text_additional_feature

SearchTextAdditionalFeatureList: TypeAlias = list[
    "capo_geo_places.types.search_text_additional_feature.SearchTextAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchTextAdditionalFeatureList) -> list:
    import capo_geo_places.types.search_text_additional_feature

    out: list = []
    for item in value:
        out.append(
            capo_geo_places.types.search_text_additional_feature.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchTextAdditionalFeatureList:
    import capo_geo_places.types.search_text_additional_feature

    out: SearchTextAdditionalFeatureList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_places.types.search_text_additional_feature.deserialize_json(item)
        )
    return out
