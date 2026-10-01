"""Generated from Smithy shape ``com.amazonaws.billing#CreditAllocationHistoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.credit_allocation_history_entry

CreditAllocationHistoryList: TypeAlias = list[
    "capo_billing.types.credit_allocation_history_entry.CreditAllocationHistoryEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreditAllocationHistoryList) -> list:
    import capo_billing.types.credit_allocation_history_entry

    out: list = []
    for item in value:
        out.append(
            capo_billing.types.credit_allocation_history_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CreditAllocationHistoryList:
    import capo_billing.types.credit_allocation_history_entry

    out: CreditAllocationHistoryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.credit_allocation_history_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out
