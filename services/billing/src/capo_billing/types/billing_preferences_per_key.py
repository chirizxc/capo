"""Generated from Smithy shape ``com.amazonaws.billing#BillingPreferencesPerKey``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.billing_preference_for_key

BillingPreferencesPerKey: TypeAlias = list[
    "capo_billing.types.billing_preference_for_key.BillingPreferenceForKey"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingPreferencesPerKey) -> list:
    import capo_billing.types.billing_preference_for_key

    out: list = []
    for item in value:
        out.append(
            capo_billing.types.billing_preference_for_key.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BillingPreferencesPerKey:
    import capo_billing.types.billing_preference_for_key

    out: BillingPreferencesPerKey = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.billing_preference_for_key.deserialize_aws_json_1_0(item)
        )
    return out
