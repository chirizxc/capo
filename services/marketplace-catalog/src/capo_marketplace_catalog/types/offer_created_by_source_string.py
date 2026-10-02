"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferCreatedBySourceString``."""

from typing import Literal, TypeAlias, cast

OfferCreatedBySourceString: TypeAlias = Literal[
    "Seller",
    "AwsMarketplace",
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferCreatedBySourceString) -> str:
    return value


def deserialize_json(data: str) -> OfferCreatedBySourceString:
    return cast(OfferCreatedBySourceString, data)
