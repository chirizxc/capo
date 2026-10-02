"""Generated from Smithy shape ``com.amazonaws.billing#ContractAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.contract_account

ContractAccountList: TypeAlias = list[
    "capo_billing.types.contract_account.ContractAccount"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContractAccountList) -> list:
    import capo_billing.types.contract_account

    out: list = []
    for item in value:
        out.append(capo_billing.types.contract_account.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ContractAccountList:
    import capo_billing.types.contract_account

    out: ContractAccountList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_billing.types.contract_account.deserialize_aws_json_1_0(item))
    return out
