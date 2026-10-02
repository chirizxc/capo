"""Generated from Smithy shape ``com.amazonaws.billing#CreditDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.credit_data

CreditDataList: TypeAlias = list["capo_billing.types.credit_data.CreditData"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreditDataList) -> list:
    import capo_billing.types.credit_data

    out: list = []
    for item in value:
        out.append(capo_billing.types.credit_data.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> CreditDataList:
    import capo_billing.types.credit_data

    out: CreditDataList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_billing.types.credit_data.deserialize_aws_json_1_0(item))
    return out
