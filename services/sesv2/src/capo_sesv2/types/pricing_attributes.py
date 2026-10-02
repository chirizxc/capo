"""Generated from Smithy shape ``com.amazonaws.sesv2#PricingAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.pricing_plan


class PricingAttributes(TypedDict, closed=True):
    current_plan: NotRequired["capo_sesv2.types.pricing_plan.PricingPlan"]
    """<p>The pricing plan that is currently active on your Amazon SES account.</p>"""
    next_plan: NotRequired["capo_sesv2.types.pricing_plan.PricingPlan"]
    """<p>The pricing plan that will become active at the start of the next monthly cycle, if a scheduled change has been requested. This field is empty when no scheduled change is pending.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PricingAttributes) -> dict:
    out: dict = {}
    if "current_plan" in value:
        import capo_sesv2.types.pricing_plan

        out["CurrentPlan"] = capo_sesv2.types.pricing_plan.serialize_json(
            value["current_plan"]
        )
    if "next_plan" in value:
        import capo_sesv2.types.pricing_plan

        out["NextPlan"] = capo_sesv2.types.pricing_plan.serialize_json(
            value["next_plan"]
        )
    return out


def deserialize_json(data: dict) -> PricingAttributes:
    out: PricingAttributes = {}  # type: ignore[typeddict-item]
    if data.get("CurrentPlan") is not None:
        import capo_sesv2.types.pricing_plan

        out["current_plan"] = capo_sesv2.types.pricing_plan.deserialize_json(
            data["CurrentPlan"]
        )
    if data.get("NextPlan") is not None:
        import capo_sesv2.types.pricing_plan

        out["next_plan"] = capo_sesv2.types.pricing_plan.deserialize_json(
            data["NextPlan"]
        )
    return out
