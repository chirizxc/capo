"""Generated from Smithy shape ``com.amazonaws.vpclattice#PayerResponsibilityPayer``."""

from typing import Literal, TypeAlias, cast

PayerResponsibilityPayer: TypeAlias = Literal[
    "VpcEndpointAccount",
    "ResourceGatewayAccount",
]


# --- restJson1 ser/de ---
def serialize_json(value: PayerResponsibilityPayer) -> str:
    return value


def deserialize_json(data: str) -> PayerResponsibilityPayer:
    return cast(PayerResponsibilityPayer, data)
