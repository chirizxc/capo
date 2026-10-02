"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferTargetAgreementIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.offer_target_agreement_id_string

OfferTargetAgreementIdFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.offer_target_agreement_id_string.OfferTargetAgreementIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferTargetAgreementIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> OfferTargetAgreementIdFilterValueList:
    return [item for item in data if item is not None]
