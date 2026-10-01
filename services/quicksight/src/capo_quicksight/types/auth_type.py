"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthType``."""

from typing import Literal, TypeAlias, cast

AuthType: TypeAlias = Literal[
    "THREE_LEGGED_OAUTH",
    "TWO_LEGGED_OAUTH",
    "SERVICE_ACCOUNT",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthType) -> str:
    return value


def deserialize_json(data: str) -> AuthType:
    return cast(AuthType, data)
