"""Generated from Smithy shape ``com.amazonaws.bedrockagent#EnabledOrDisabledState``."""

from typing import Literal, TypeAlias, cast

EnabledOrDisabledState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledOrDisabledState) -> str:
    return value


def deserialize_json(data: str) -> EnabledOrDisabledState:
    return cast(EnabledOrDisabledState, data)
