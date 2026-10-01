"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferCreatedBySourceFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.offer_created_by_source_string

OfferCreatedBySourceFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.offer_created_by_source_string.OfferCreatedBySourceString"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferCreatedBySourceFilterValueList) -> list:
    import capo_marketplace_catalog.types.offer_created_by_source_string

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_catalog.types.offer_created_by_source_string.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OfferCreatedBySourceFilterValueList:
    import capo_marketplace_catalog.types.offer_created_by_source_string

    out: OfferCreatedBySourceFilterValueList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_catalog.types.offer_created_by_source_string.deserialize_json(
                item
            )
        )
    return out
