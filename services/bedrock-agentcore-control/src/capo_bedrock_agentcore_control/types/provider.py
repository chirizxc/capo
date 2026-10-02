"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Provider``."""

from typing import Literal, TypeAlias, cast

Provider: TypeAlias = Literal[
    "AWS",
    "DeepEval",
    "AutoEval",
    "Custom",
]


# --- restJson1 ser/de ---
def serialize_json(value: Provider) -> str:
    return value


def deserialize_json(data: str) -> Provider:
    return cast(Provider, data)
