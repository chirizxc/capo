"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationIssuerAccountIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resale_authorization_issuer_account_id_string

ResaleAuthorizationIssuerAccountIdFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.resale_authorization_issuer_account_id_string.ResaleAuthorizationIssuerAccountIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationIssuerAccountIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResaleAuthorizationIssuerAccountIdFilterValueList:
    return [item for item in data if item is not None]
