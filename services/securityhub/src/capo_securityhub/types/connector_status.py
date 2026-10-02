"""Generated from Smithy shape ``com.amazonaws.securityhub#ConnectorStatus``."""

from typing import Literal, TypeAlias, cast

ConnectorStatus: TypeAlias = Literal[
    "CONNECTED",
    "DEGRADED",
    "FAILED_TO_CONNECT",
    "PENDING_AUTHORIZATION",
    "PENDING_CONFIGURATION",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorStatus) -> str:
    return value


def deserialize_json(data: str) -> ConnectorStatus:
    return cast(ConnectorStatus, data)
