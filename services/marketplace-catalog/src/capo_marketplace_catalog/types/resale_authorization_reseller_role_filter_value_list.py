"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationResellerRoleFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resale_authorization_reseller_role_string

ResaleAuthorizationResellerRoleFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.resale_authorization_reseller_role_string.ResaleAuthorizationResellerRoleString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationResellerRoleFilterValueList) -> list:
    import capo_marketplace_catalog.types.resale_authorization_reseller_role_string

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_catalog.types.resale_authorization_reseller_role_string.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResaleAuthorizationResellerRoleFilterValueList:
    import capo_marketplace_catalog.types.resale_authorization_reseller_role_string

    out: ResaleAuthorizationResellerRoleFilterValueList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_catalog.types.resale_authorization_reseller_role_string.deserialize_json(
                item
            )
        )
    return out
