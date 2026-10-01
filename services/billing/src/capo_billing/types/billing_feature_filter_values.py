"""Generated from Smithy shape ``com.amazonaws.billing#BillingFeatureFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.billing_feature_filter_value

BillingFeatureFilterValues: TypeAlias = list[
    "capo_billing.types.billing_feature_filter_value.BillingFeatureFilterValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingFeatureFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> BillingFeatureFilterValues:
    return [item for item in data if item is not None]
