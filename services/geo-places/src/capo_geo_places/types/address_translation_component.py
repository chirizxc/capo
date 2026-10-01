"""Generated from Smithy shape ``com.amazonaws.geoplaces#AddressTranslationComponent``."""

from typing import Literal, TypeAlias, cast

AddressTranslationComponent: TypeAlias = Literal[
    "District",
    "Locality",
    "Region",
    "SubRegion",
]


# --- restJson1 ser/de ---
def serialize_json(value: AddressTranslationComponent) -> str:
    return value


def deserialize_json(data: str) -> AddressTranslationComponent:
    return cast(AddressTranslationComponent, data)
