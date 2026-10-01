"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessHookEventType``."""

from typing import Literal, TypeAlias, cast

HarnessHookEventType: TypeAlias = Literal[
    "before_tool_call",
    "after_tool_call",
    "before_invocation",
    "after_invocation",
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessHookEventType) -> str:
    return value


def deserialize_json(data: str) -> HarnessHookEventType:
    return cast(HarnessHookEventType, data)
