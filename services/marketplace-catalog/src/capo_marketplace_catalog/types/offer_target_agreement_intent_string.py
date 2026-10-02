"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferTargetAgreementIntentString``."""

from typing import Literal, TypeAlias, cast

OfferTargetAgreementIntentString: TypeAlias = Literal["Renew",]


# --- restJson1 ser/de ---
def serialize_json(value: OfferTargetAgreementIntentString) -> str:
    return value


def deserialize_json(data: str) -> OfferTargetAgreementIntentString:
    return cast(OfferTargetAgreementIntentString, data)
