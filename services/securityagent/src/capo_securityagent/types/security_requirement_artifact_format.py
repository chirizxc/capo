"""Generated from Smithy shape ``com.amazonaws.securityagent#SecurityRequirementArtifactFormat``."""

from typing import Literal, TypeAlias, cast

SecurityRequirementArtifactFormat: TypeAlias = Literal[
    "MD",
    "PDF",
    "TXT",
    "DOCX",
    "DOC",
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityRequirementArtifactFormat) -> str:
    return value


def deserialize_json(data: str) -> SecurityRequirementArtifactFormat:
    return cast(SecurityRequirementArtifactFormat, data)
