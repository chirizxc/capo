"""Generated from Smithy shape ``com.amazonaws.geomaps#PoiCategory``."""

from typing import Literal, TypeAlias, cast

PoiCategory: TypeAlias = Literal[
    "FoodAndDrink",
    "Entertainment",
    "SightsAndMuseums",
    "Transportation",
    "Accommodations",
    "LeisureAndOutdoor",
    "Shopping",
    "BusinessAndServices",
    "FacilitiesAndBuildings",
]


# --- restJson1 ser/de ---
def serialize_json(value: PoiCategory) -> str:
    return value


def deserialize_json(data: str) -> PoiCategory:
    return cast(PoiCategory, data)
