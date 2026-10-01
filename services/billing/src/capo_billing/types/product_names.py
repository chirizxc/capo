"""Generated from Smithy shape ``com.amazonaws.billing#ProductNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.product_name

ProductNames: TypeAlias = list["capo_billing.types.product_name.ProductName"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProductNames) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ProductNames:
    return [item for item in data if item is not None]
