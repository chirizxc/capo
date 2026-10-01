"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdateTieringInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_tiers_list
    import capo_billingconductor.types.update_free_tier_config


class UpdateTieringInput(TypedDict, closed=True):
    free_tier: NotRequired[
        "capo_billingconductor.types.update_free_tier_config.UpdateFreeTierConfig"
    ]
    """<p> The possible Amazon Web Services Free Tier configurations. </p>"""
    custom_tiers: NotRequired[
        "capo_billingconductor.types.custom_tiers_list.CustomTiersList"
    ]
    """<p> The set of custom tiers for the pricing rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTieringInput) -> dict:
    out: dict = {}
    if "free_tier" in value:
        import capo_billingconductor.types.update_free_tier_config

        out["FreeTier"] = (
            capo_billingconductor.types.update_free_tier_config.serialize_json(
                value["free_tier"]
            )
        )
    if "custom_tiers" in value:
        import capo_billingconductor.types.custom_tiers_list

        out["CustomTiers"] = (
            capo_billingconductor.types.custom_tiers_list.serialize_json(
                value["custom_tiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateTieringInput:
    out: UpdateTieringInput = {}  # type: ignore[typeddict-item]
    if data.get("FreeTier") is not None:
        import capo_billingconductor.types.update_free_tier_config

        out["free_tier"] = (
            capo_billingconductor.types.update_free_tier_config.deserialize_json(
                data["FreeTier"]
            )
        )
    if data.get("CustomTiers") is not None:
        import capo_billingconductor.types.custom_tiers_list

        out["custom_tiers"] = (
            capo_billingconductor.types.custom_tiers_list.deserialize_json(
                data["CustomTiers"]
            )
        )
    return out
