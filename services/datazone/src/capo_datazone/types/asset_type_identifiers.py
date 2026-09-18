"""Generated from Smithy shape ``com.amazonaws.datazone#AssetTypeIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.asset_type_identifier

AssetTypeIdentifiers: TypeAlias = list[
    "capo_datazone.types.asset_type_identifier.AssetTypeIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetTypeIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> AssetTypeIdentifiers:
    return [item for item in data if item is not None]
