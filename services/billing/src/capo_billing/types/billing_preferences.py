"""Generated from Smithy shape ``com.amazonaws.billing#BillingPreferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.billing_preference_summary

BillingPreferences: TypeAlias = list[
    "capo_billing.types.billing_preference_summary.BillingPreferenceSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingPreferences) -> list:
    import capo_billing.types.billing_preference_summary

    out: list = []
    for item in value:
        out.append(
            capo_billing.types.billing_preference_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BillingPreferences:
    import capo_billing.types.billing_preference_summary

    out: BillingPreferences = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.billing_preference_summary.deserialize_aws_json_1_0(item)
        )
    return out
