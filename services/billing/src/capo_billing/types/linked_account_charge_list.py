"""Generated from Smithy shape ``com.amazonaws.billing#LinkedAccountChargeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.linked_account_charge

LinkedAccountChargeList: TypeAlias = list[
    "capo_billing.types.linked_account_charge.LinkedAccountCharge"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LinkedAccountChargeList) -> list:
    import capo_billing.types.linked_account_charge

    out: list = []
    for item in value:
        out.append(
            capo_billing.types.linked_account_charge.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LinkedAccountChargeList:
    import capo_billing.types.linked_account_charge

    out: LinkedAccountChargeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.linked_account_charge.deserialize_aws_json_1_0(item)
        )
    return out
