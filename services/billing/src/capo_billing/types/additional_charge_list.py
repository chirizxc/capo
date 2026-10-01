"""Generated from Smithy shape ``com.amazonaws.billing#AdditionalChargeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.additional_charge

AdditionalChargeList: TypeAlias = list[
    "capo_billing.types.additional_charge.AdditionalCharge"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AdditionalChargeList) -> list:
    import capo_billing.types.additional_charge

    out: list = []
    for item in value:
        out.append(capo_billing.types.additional_charge.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> AdditionalChargeList:
    import capo_billing.types.additional_charge

    out: AdditionalChargeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_billing.types.additional_charge.deserialize_aws_json_1_0(item))
    return out
