"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#RevocationMode``."""

from typing import Literal, TypeAlias, cast

RevocationMode: TypeAlias = Literal[
    "REVOKE_URL",
    "REVOKE_AND_TERMINATE_SESSIONS",
]


# --- restJson1 ser/de ---
def serialize_json(value: RevocationMode) -> str:
    return value


def deserialize_json(data: str) -> RevocationMode:
    return cast(RevocationMode, data)
