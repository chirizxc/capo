"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ErrorScopeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.error_scope

ErrorScopeList: TypeAlias = list[
    "capo_marketplace_catalog.types.error_scope.ErrorScope"
]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorScopeList) -> list:
    import capo_marketplace_catalog.types.error_scope

    out: list = []
    for item in value:
        out.append(capo_marketplace_catalog.types.error_scope.serialize_json(item))
    return out


def deserialize_json(data: list) -> ErrorScopeList:
    import capo_marketplace_catalog.types.error_scope

    out: ErrorScopeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_marketplace_catalog.types.error_scope.deserialize_json(item))
    return out
