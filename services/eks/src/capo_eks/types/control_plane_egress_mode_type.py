"""Generated from Smithy shape ``com.amazonaws.eks#ControlPlaneEgressModeType``."""

from typing import Literal, TypeAlias, cast

ControlPlaneEgressModeType: TypeAlias = Literal[
    "AWS_MANAGED",
    "CUSTOMER_ROUTED",
    "CUSTOMER_ISOLATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlPlaneEgressModeType) -> str:
    return value


def deserialize_json(data: str) -> ControlPlaneEgressModeType:
    return cast(ControlPlaneEgressModeType, data)
