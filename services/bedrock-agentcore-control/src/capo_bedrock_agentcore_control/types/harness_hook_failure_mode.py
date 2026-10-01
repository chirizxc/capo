"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessHookFailureMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The behavior when a synchronous hook target fails.</p>"""
HarnessHookFailureMode: TypeAlias = Literal[
    "allow",
    "deny",
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessHookFailureMode) -> str:
    return value


def deserialize_json(data: str) -> HarnessHookFailureMode:
    return cast(HarnessHookFailureMode, data)
