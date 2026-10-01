"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferTargetAgreementIntentFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.offer_target_agreement_intent_string

OfferTargetAgreementIntentFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.offer_target_agreement_intent_string.OfferTargetAgreementIntentString"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferTargetAgreementIntentFilterValueList) -> list:
    import capo_marketplace_catalog.types.offer_target_agreement_intent_string

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_catalog.types.offer_target_agreement_intent_string.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OfferTargetAgreementIntentFilterValueList:
    import capo_marketplace_catalog.types.offer_target_agreement_intent_string

    out: OfferTargetAgreementIntentFilterValueList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_catalog.types.offer_target_agreement_intent_string.deserialize_json(
                item
            )
        )
    return out
