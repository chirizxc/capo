"""Generated from Smithy shape ``com.amazonaws.securityagent#ValidationStatus``."""

from typing import Literal, TypeAlias, cast

"""Per-finding sandbox validation status"""
ValidationStatus: TypeAlias = Literal[
    "CONFIRMED",
    "NOT_REPRODUCED",
    "VALIDATION_FAILED",
    "VALIDATING",
    "NOT_VALIDATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationStatus) -> str:
    return value


def deserialize_json(data: str) -> ValidationStatus:
    return cast(ValidationStatus, data)
