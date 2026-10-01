"""Generated from Smithy shape ``com.amazonaws.securityhub#HealthIssueCode``."""

from typing import Literal, TypeAlias, cast

"""<p>The error code for a connector health issue.</p>"""
HealthIssueCode: TypeAlias = Literal[
    "AUTHENTICATION_FAILURE",
    "STREAM_AUTHORIZATION_FAILURE",
    "DISCOVERY_FAILURE",
    "STREAM_LIMIT_EXCEEDED",
    "STREAM_DISCONNECTED",
    "RECORDING_FAILURE",
    "NO_HEALTH_DATA",
]


# --- restJson1 ser/de ---
def serialize_json(value: HealthIssueCode) -> str:
    return value


def deserialize_json(data: str) -> HealthIssueCode:
    return cast(HealthIssueCode, data)
