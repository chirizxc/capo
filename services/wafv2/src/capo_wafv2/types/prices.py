"""Generated from Smithy shape ``com.amazonaws.wafv2#Prices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.price

Prices: TypeAlias = list["capo_wafv2.types.price.Price"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Prices) -> list:
    import capo_wafv2.types.price

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.price.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Prices:
    import capo_wafv2.types.price

    out: Prices = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wafv2.types.price.deserialize_aws_json_1_1(item))
    return out
