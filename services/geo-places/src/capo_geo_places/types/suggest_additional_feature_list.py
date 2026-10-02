"""Generated from Smithy shape ``com.amazonaws.geoplaces#SuggestAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.suggest_additional_feature

SuggestAdditionalFeatureList: TypeAlias = list[
    "capo_geo_places.types.suggest_additional_feature.SuggestAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuggestAdditionalFeatureList) -> list:
    import capo_geo_places.types.suggest_additional_feature

    out: list = []
    for item in value:
        out.append(
            capo_geo_places.types.suggest_additional_feature.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SuggestAdditionalFeatureList:
    import capo_geo_places.types.suggest_additional_feature

    out: SuggestAdditionalFeatureList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_places.types.suggest_additional_feature.deserialize_json(item)
        )
    return out
