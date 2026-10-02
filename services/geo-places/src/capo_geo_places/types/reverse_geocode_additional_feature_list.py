"""Generated from Smithy shape ``com.amazonaws.geoplaces#ReverseGeocodeAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.reverse_geocode_additional_feature

ReverseGeocodeAdditionalFeatureList: TypeAlias = list[
    "capo_geo_places.types.reverse_geocode_additional_feature.ReverseGeocodeAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReverseGeocodeAdditionalFeatureList) -> list:
    import capo_geo_places.types.reverse_geocode_additional_feature

    out: list = []
    for item in value:
        out.append(
            capo_geo_places.types.reverse_geocode_additional_feature.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ReverseGeocodeAdditionalFeatureList:
    import capo_geo_places.types.reverse_geocode_additional_feature

    out: ReverseGeocodeAdditionalFeatureList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_places.types.reverse_geocode_additional_feature.deserialize_json(
                item
            )
        )
    return out
