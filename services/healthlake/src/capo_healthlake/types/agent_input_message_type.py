"""Generated from Smithy shape ``com.amazonaws.healthlake#AgentInputMessageType``."""

from typing import Literal, TypeAlias, cast

AgentInputMessageType: TypeAlias = Literal[
    "normal",
    "confirmation_response",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgentInputMessageType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AgentInputMessageType:
    return cast(AgentInputMessageType, data)
