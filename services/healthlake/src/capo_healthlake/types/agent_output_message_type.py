"""Generated from Smithy shape ``com.amazonaws.healthlake#AgentOutputMessageType``."""

from typing import Literal, TypeAlias, cast

AgentOutputMessageType: TypeAlias = Literal[
    "INITIAL_GREETING",
    "normal",
    "confirmation",
    "complete",
    "error",
    "options",
    "choices",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgentOutputMessageType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AgentOutputMessageType:
    return cast(AgentOutputMessageType, data)
