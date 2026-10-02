"""Generated from Smithy shape ``com.amazonaws.cleanrooms#InheritedAllowedResultReceiversSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.inherited_allowed_result_receivers_source

InheritedAllowedResultReceiversSourceList: TypeAlias = list[
    "capo_cleanrooms.types.inherited_allowed_result_receivers_source.InheritedAllowedResultReceiversSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: InheritedAllowedResultReceiversSourceList) -> list:
    import capo_cleanrooms.types.inherited_allowed_result_receivers_source

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.inherited_allowed_result_receivers_source.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InheritedAllowedResultReceiversSourceList:
    import capo_cleanrooms.types.inherited_allowed_result_receivers_source

    out: InheritedAllowedResultReceiversSourceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cleanrooms.types.inherited_allowed_result_receivers_source.deserialize_json(
                item
            )
        )
    return out
