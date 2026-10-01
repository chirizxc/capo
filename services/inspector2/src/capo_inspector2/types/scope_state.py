"""Generated from Smithy shape ``com.amazonaws.inspector2#ScopeState``."""

from typing import Literal, TypeAlias, cast

ScopeState: TypeAlias = Literal[
    "ACTIVE",
    "PENDING",
    "ERROR",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScopeState) -> str:
    return value


def deserialize_json(data: str) -> ScopeState:
    return cast(ScopeState, data)
