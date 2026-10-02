"""Generated from Smithy shape ``com.amazonaws.securityagent#SecurityRequirementPackImportStatus``."""

from typing import Literal, TypeAlias, cast

SecurityRequirementPackImportStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityRequirementPackImportStatus) -> str:
    return value


def deserialize_json(data: str) -> SecurityRequirementPackImportStatus:
    return cast(SecurityRequirementPackImportStatus, data)
