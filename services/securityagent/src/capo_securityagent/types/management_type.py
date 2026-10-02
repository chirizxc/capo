"""Generated from Smithy shape ``com.amazonaws.securityagent#ManagementType``."""

from typing import Literal, TypeAlias, cast

ManagementType: TypeAlias = Literal[
    "AWS_MANAGED",
    "CUSTOMER_MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagementType) -> str:
    return value


def deserialize_json(data: str) -> ManagementType:
    return cast(ManagementType, data)
