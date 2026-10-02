"""Generated from Smithy shape ``com.amazonaws.geomaps#TileAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_maps.types.tile_additional_feature

TileAdditionalFeatureList: TypeAlias = list[
    "capo_geo_maps.types.tile_additional_feature.TileAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: TileAdditionalFeatureList) -> list:
    import capo_geo_maps.types.tile_additional_feature

    out: list = []
    for item in value:
        out.append(capo_geo_maps.types.tile_additional_feature.serialize_json(item))
    return out


def deserialize_json(data: list) -> TileAdditionalFeatureList:
    import capo_geo_maps.types.tile_additional_feature

    out: TileAdditionalFeatureList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_maps.types.tile_additional_feature.deserialize_json(item))
    return out
