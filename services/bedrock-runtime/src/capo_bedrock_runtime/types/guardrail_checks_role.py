"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksRole``."""

from typing import Literal, TypeAlias, cast

"""<p>The role of the message sender in the conversation.</p>"""
GuardrailChecksRole: TypeAlias = Literal[
    "user",
    "assistant",
    "system",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksRole) -> str:
    return value


def deserialize_json(data: str) -> GuardrailChecksRole:
    return cast(GuardrailChecksRole, data)
