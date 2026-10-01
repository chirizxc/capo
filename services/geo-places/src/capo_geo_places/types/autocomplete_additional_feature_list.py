"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.autocomplete_additional_feature

AutocompleteAdditionalFeatureList: TypeAlias = list[
    "capo_geo_places.types.autocomplete_additional_feature.AutocompleteAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteAdditionalFeatureList) -> list:
    import capo_geo_places.types.autocomplete_additional_feature

    out: list = []
    for item in value:
        out.append(
            capo_geo_places.types.autocomplete_additional_feature.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutocompleteAdditionalFeatureList:
    import capo_geo_places.types.autocomplete_additional_feature

    out: AutocompleteAdditionalFeatureList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_places.types.autocomplete_additional_feature.deserialize_json(item)
        )
    return out
