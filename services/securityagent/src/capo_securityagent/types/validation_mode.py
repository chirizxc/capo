"""Generated from Smithy shape ``com.amazonaws.securityagent#ValidationMode``."""

from typing import Literal, TypeAlias, cast

"""Mode of validation to perform on findings"""
ValidationMode: TypeAlias = Literal[
    "DISABLED",
    "SIMULATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationMode) -> str:
    return value


def deserialize_json(data: str) -> ValidationMode:
    return cast(ValidationMode, data)
