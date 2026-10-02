"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Monitoring``."""

from typing import Literal, TypeAlias, cast

Monitoring: TypeAlias = Literal[
    "BASIC",
    "DETAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Monitoring) -> str:
    return value


def deserialize_json(data: str) -> Monitoring:
    return cast(Monitoring, data)
