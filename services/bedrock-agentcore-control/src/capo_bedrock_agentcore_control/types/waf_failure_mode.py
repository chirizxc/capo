"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#WafFailureMode``."""

from typing import Literal, TypeAlias, cast

WafFailureMode: TypeAlias = Literal[
    "FAIL_CLOSE",
    "FAIL_OPEN",
]


# --- restJson1 ser/de ---
def serialize_json(value: WafFailureMode) -> str:
    return value


def deserialize_json(data: str) -> WafFailureMode:
    return cast(WafFailureMode, data)
