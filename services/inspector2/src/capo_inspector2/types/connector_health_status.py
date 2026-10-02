"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorHealthStatus``."""

from typing import Literal, TypeAlias, cast

ConnectorHealthStatus: TypeAlias = Literal[
    "CONNECTED",
    "DEGRADED",
    "FAILED_TO_CONNECT",
    "PENDING_AUTHORIZATION",
    "PENDING_CONFIGURATION",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorHealthStatus) -> str:
    return value


def deserialize_json(data: str) -> ConnectorHealthStatus:
    return cast(ConnectorHealthStatus, data)
