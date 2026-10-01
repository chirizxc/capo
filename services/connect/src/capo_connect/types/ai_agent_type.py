"""Generated from Smithy shape ``com.amazonaws.connect#AIAgentType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of the AI agent.</p>"""
AIAgentType: TypeAlias = Literal["THIRD_PARTY",]


# --- restJson1 ser/de ---
def serialize_json(value: AIAgentType) -> str:
    return value


def deserialize_json(data: str) -> AIAgentType:
    return cast(AIAgentType, data)
