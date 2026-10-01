"""Generated from Smithy shape ``com.amazonaws.securityagent#SecurityRequirementPackStatus``."""

from typing import Literal, TypeAlias, cast

SecurityRequirementPackStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityRequirementPackStatus) -> str:
    return value


def deserialize_json(data: str) -> SecurityRequirementPackStatus:
    return cast(SecurityRequirementPackStatus, data)
