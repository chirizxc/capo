"""Generated from Smithy shape ``com.amazonaws.vpclattice#PayerResponsibilityScope``."""

from typing import Literal, TypeAlias, cast

PayerResponsibilityScope: TypeAlias = Literal["ResourceGatewayCharges",]


# --- restJson1 ser/de ---
def serialize_json(value: PayerResponsibilityScope) -> str:
    return value


def deserialize_json(data: str) -> PayerResponsibilityScope:
    return cast(PayerResponsibilityScope, data)
