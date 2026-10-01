"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationSourceAuthorizationFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resale_authorization_source_authorization_string

ResaleAuthorizationSourceAuthorizationFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.resale_authorization_source_authorization_string.ResaleAuthorizationSourceAuthorizationString"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: ResaleAuthorizationSourceAuthorizationFilterValueList,
) -> list:
    return list(value)


def deserialize_json(
    data: list,
) -> ResaleAuthorizationSourceAuthorizationFilterValueList:
    return [item for item in data if item is not None]
