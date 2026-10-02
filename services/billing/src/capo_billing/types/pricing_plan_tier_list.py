"""Generated from Smithy shape ``com.amazonaws.billing#PricingPlanTierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.pricing_plan_tier

PricingPlanTierList: TypeAlias = list[
    "capo_billing.types.pricing_plan_tier.PricingPlanTier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PricingPlanTierList) -> list:
    import capo_billing.types.pricing_plan_tier

    out: list = []
    for item in value:
        out.append(capo_billing.types.pricing_plan_tier.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> PricingPlanTierList:
    import capo_billing.types.pricing_plan_tier

    out: PricingPlanTierList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_billing.types.pricing_plan_tier.deserialize_aws_json_1_0(item))
    return out
