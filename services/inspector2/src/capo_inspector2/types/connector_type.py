"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorType``."""

from typing import Literal, TypeAlias, cast

ConnectorType: TypeAlias = Literal[
    "CUSTOMER_MANAGED",
    "SERVICE_LINKED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorType) -> str:
    return value


def deserialize_json(data: str) -> ConnectorType:
    return cast(ConnectorType, data)
