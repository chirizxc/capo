"""Generated from Smithy shape ``com.amazonaws.opensearch#SavedObjectIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.saved_object_identifier

SavedObjectIdentifierList: TypeAlias = list[
    "capo_opensearch.types.saved_object_identifier.SavedObjectIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavedObjectIdentifierList) -> list:
    import capo_opensearch.types.saved_object_identifier

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.saved_object_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> SavedObjectIdentifierList:
    import capo_opensearch.types.saved_object_identifier

    out: SavedObjectIdentifierList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_opensearch.types.saved_object_identifier.deserialize_json(item))
    return out
