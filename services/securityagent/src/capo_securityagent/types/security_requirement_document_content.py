"""Generated from Smithy shape ``com.amazonaws.securityagent#SecurityRequirementDocumentContent``."""

import base64
from typing import TypeAlias

SecurityRequirementDocumentContent: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: SecurityRequirementDocumentContent) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> SecurityRequirementDocumentContent:
    return base64.b64decode(data)
