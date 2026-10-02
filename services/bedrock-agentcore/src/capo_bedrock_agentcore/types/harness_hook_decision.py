"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessHookDecision``."""

from typing import Literal, TypeAlias, cast

HarnessHookDecision: TypeAlias = Literal[
    "allow",
    "deny",
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessHookDecision) -> str:
    return value


def deserialize_json(data: str) -> HarnessHookDecision:
    return cast(HarnessHookDecision, data)
