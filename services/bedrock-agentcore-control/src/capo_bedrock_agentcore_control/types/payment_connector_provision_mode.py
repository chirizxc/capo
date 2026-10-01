"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentConnectorProvisionMode``."""

from typing import Literal, TypeAlias, cast

PaymentConnectorProvisionMode: TypeAlias = Literal[
    "MANUAL",
    "QUICK_CREATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentConnectorProvisionMode) -> str:
    return value


def deserialize_json(data: str) -> PaymentConnectorProvisionMode:
    return cast(PaymentConnectorProvisionMode, data)
