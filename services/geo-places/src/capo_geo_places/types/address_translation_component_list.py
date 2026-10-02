"""Generated from Smithy shape ``com.amazonaws.geoplaces#AddressTranslationComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.address_translation_component

AddressTranslationComponentList: TypeAlias = list[
    "capo_geo_places.types.address_translation_component.AddressTranslationComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: AddressTranslationComponentList) -> list:
    import capo_geo_places.types.address_translation_component

    out: list = []
    for item in value:
        out.append(
            capo_geo_places.types.address_translation_component.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AddressTranslationComponentList:
    import capo_geo_places.types.address_translation_component

    out: AddressTranslationComponentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_places.types.address_translation_component.deserialize_json(item)
        )
    return out
