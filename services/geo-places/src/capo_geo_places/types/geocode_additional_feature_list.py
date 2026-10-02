"""Generated from Smithy shape ``com.amazonaws.geoplaces#GeocodeAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.geocode_additional_feature

GeocodeAdditionalFeatureList: TypeAlias = list[
    "capo_geo_places.types.geocode_additional_feature.GeocodeAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeocodeAdditionalFeatureList) -> list:
    import capo_geo_places.types.geocode_additional_feature

    out: list = []
    for item in value:
        out.append(
            capo_geo_places.types.geocode_additional_feature.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GeocodeAdditionalFeatureList:
    import capo_geo_places.types.geocode_additional_feature

    out: GeocodeAdditionalFeatureList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_places.types.geocode_additional_feature.deserialize_json(item)
        )
    return out
