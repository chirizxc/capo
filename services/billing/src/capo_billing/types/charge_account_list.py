"""Generated from Smithy shape ``com.amazonaws.billing#ChargeAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.charge_account

ChargeAccountList: TypeAlias = list["capo_billing.types.charge_account.ChargeAccount"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChargeAccountList) -> list:
    import capo_billing.types.charge_account

    out: list = []
    for item in value:
        out.append(capo_billing.types.charge_account.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ChargeAccountList:
    import capo_billing.types.charge_account

    out: ChargeAccountList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_billing.types.charge_account.deserialize_aws_json_1_0(item))
    return out
