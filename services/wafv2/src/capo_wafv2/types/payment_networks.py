"""Generated from Smithy shape ``com.amazonaws.wafv2#PaymentNetworks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.payment_network

PaymentNetworks: TypeAlias = list["capo_wafv2.types.payment_network.PaymentNetwork"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PaymentNetworks) -> list:
    import capo_wafv2.types.payment_network

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.payment_network.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PaymentNetworks:
    import capo_wafv2.types.payment_network

    out: PaymentNetworks = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wafv2.types.payment_network.deserialize_aws_json_1_1(item))
    return out
