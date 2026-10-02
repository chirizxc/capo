"""Generated from Smithy shape ``com.amazonaws.geomaps#PoiCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_maps.types.poi_category

PoiCategoryList: TypeAlias = list["capo_geo_maps.types.poi_category.PoiCategory"]


# --- restJson1 ser/de ---
def serialize_json(value: PoiCategoryList) -> list:
    import capo_geo_maps.types.poi_category

    out: list = []
    for item in value:
        out.append(capo_geo_maps.types.poi_category.serialize_json(item))
    return out


def deserialize_json(data: list) -> PoiCategoryList:
    import capo_geo_maps.types.poi_category

    out: PoiCategoryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_maps.types.poi_category.deserialize_json(item))
    return out
