"""Generated from Smithy shape ``com.amazonaws.billing#PurchaseTypeApplications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.purchase_type

PurchaseTypeApplications: TypeAlias = list[
    "capo_billing.types.purchase_type.PurchaseType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PurchaseTypeApplications) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> PurchaseTypeApplications:
    return [item for item in data if item is not None]
