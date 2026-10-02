"""Generated from Smithy shape ``com.amazonaws.billing#BillingFeatureFilterName``."""

from typing import Literal, TypeAlias, cast

BillingFeatureFilterName: TypeAlias = Literal["PREFERENCE_KEY",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingFeatureFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingFeatureFilterName:
    return cast(BillingFeatureFilterName, data)
