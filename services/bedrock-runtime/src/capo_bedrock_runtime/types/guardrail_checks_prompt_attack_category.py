"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksPromptAttackCategory``."""

from typing import Literal, TypeAlias, cast

"""<p>The category for prompt attack evaluation.</p>"""
GuardrailChecksPromptAttackCategory: TypeAlias = Literal[
    "JAILBREAK",
    "PROMPT_INJECTION",
    "PROMPT_LEAKAGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksPromptAttackCategory) -> str:
    return value


def deserialize_json(data: str) -> GuardrailChecksPromptAttackCategory:
    return cast(GuardrailChecksPromptAttackCategory, data)
