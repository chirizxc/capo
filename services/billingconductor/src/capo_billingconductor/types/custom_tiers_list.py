"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomTiersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_tier

CustomTiersList: TypeAlias = list["capo_billingconductor.types.custom_tier.CustomTier"]


# --- restJson1 ser/de ---
def serialize_json(value: CustomTiersList) -> list:
    import capo_billingconductor.types.custom_tier

    out: list = []
    for item in value:
        out.append(capo_billingconductor.types.custom_tier.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomTiersList:
    import capo_billingconductor.types.custom_tier

    out: CustomTiersList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_billingconductor.types.custom_tier.deserialize_json(item))
    return out
