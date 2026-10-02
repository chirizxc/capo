"""Generated from Smithy shape ``com.amazonaws.billing#TimePeriodList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.enterprise_support_time_period

TimePeriodList: TypeAlias = list[
    "capo_billing.types.enterprise_support_time_period.EnterpriseSupportTimePeriod"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimePeriodList) -> list:
    import capo_billing.types.enterprise_support_time_period

    out: list = []
    for item in value:
        out.append(
            capo_billing.types.enterprise_support_time_period.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TimePeriodList:
    import capo_billing.types.enterprise_support_time_period

    out: TimePeriodList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.enterprise_support_time_period.deserialize_aws_json_1_0(
                item
            )
        )
    return out
