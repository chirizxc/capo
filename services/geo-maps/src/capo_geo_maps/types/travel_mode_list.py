"""Generated from Smithy shape ``com.amazonaws.geomaps#TravelModeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_maps.types.travel_mode

TravelModeList: TypeAlias = list["capo_geo_maps.types.travel_mode.TravelMode"]


# --- restJson1 ser/de ---
def serialize_json(value: TravelModeList) -> list:
    import capo_geo_maps.types.travel_mode

    out: list = []
    for item in value:
        out.append(capo_geo_maps.types.travel_mode.serialize_json(item))
    return out


def deserialize_json(data: list) -> TravelModeList:
    import capo_geo_maps.types.travel_mode

    out: TravelModeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_maps.types.travel_mode.deserialize_json(item))
    return out
