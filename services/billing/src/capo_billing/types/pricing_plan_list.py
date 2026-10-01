"""Generated from Smithy shape ``com.amazonaws.billing#PricingPlanList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.pricing_plan

PricingPlanList: TypeAlias = list["capo_billing.types.pricing_plan.PricingPlan"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PricingPlanList) -> list:
    import capo_billing.types.pricing_plan

    out: list = []
    for item in value:
        out.append(capo_billing.types.pricing_plan.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> PricingPlanList:
    import capo_billing.types.pricing_plan

    out: PricingPlanList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_billing.types.pricing_plan.deserialize_aws_json_1_0(item))
    return out
