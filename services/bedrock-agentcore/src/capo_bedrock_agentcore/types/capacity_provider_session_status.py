"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CapacityProviderSessionStatus``."""

from typing import Literal, TypeAlias, cast

CapacityProviderSessionStatus: TypeAlias = Literal[
    "Provisioning",
    "Deprovisioning",
    "Active",
    "Deleting",
    "Deleted",
    "Stopped",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderSessionStatus) -> str:
    return value


def deserialize_json(data: str) -> CapacityProviderSessionStatus:
    return cast(CapacityProviderSessionStatus, data)
