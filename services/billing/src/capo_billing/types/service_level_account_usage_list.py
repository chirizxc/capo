"""Generated from Smithy shape ``com.amazonaws.billing#ServiceLevelAccountUsageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.service_level_account_usage

ServiceLevelAccountUsageList: TypeAlias = list[
    "capo_billing.types.service_level_account_usage.ServiceLevelAccountUsage"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceLevelAccountUsageList) -> list:
    import capo_billing.types.service_level_account_usage

    out: list = []
    for item in value:
        out.append(
            capo_billing.types.service_level_account_usage.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ServiceLevelAccountUsageList:
    import capo_billing.types.service_level_account_usage

    out: ServiceLevelAccountUsageList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.service_level_account_usage.deserialize_aws_json_1_0(
                item
            )
        )
    return out
