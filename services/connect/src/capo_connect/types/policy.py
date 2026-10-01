"""Generated from Smithy shape ``com.amazonaws.connect#Policy``."""

from typing import Literal, TypeAlias, cast

Policy: TypeAlias = Literal[
    "None",
    "RedactedOnly",
    "RedactedAndOriginal",
]


# --- restJson1 ser/de ---
def serialize_json(value: Policy) -> str:
    return value


def deserialize_json(data: str) -> Policy:
    return cast(Policy, data)
