"""Generated from Smithy shape ``com.amazonaws.ssm#AzureSubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.azure_subscription

AzureSubscriptionList: TypeAlias = list[
    "capo_ssm.types.azure_subscription.AzureSubscription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AzureSubscriptionList) -> list:
    import capo_ssm.types.azure_subscription

    out: list = []
    for item in value:
        out.append(capo_ssm.types.azure_subscription.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AzureSubscriptionList:
    import capo_ssm.types.azure_subscription

    out: AzureSubscriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.azure_subscription.deserialize_aws_json_1_1(item))
    return out
