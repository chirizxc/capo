"""Generated from Smithy shape ``com.amazonaws.billing#FailedMonthsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.billing_month

FailedMonthsList: TypeAlias = list["capo_billing.types.billing_month.BillingMonth"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FailedMonthsList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> FailedMonthsList:
    return [item for item in data if item is not None]
