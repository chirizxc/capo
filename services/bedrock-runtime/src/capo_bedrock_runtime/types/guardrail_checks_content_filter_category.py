"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksContentFilterCategory``."""

from typing import Literal, TypeAlias, cast

"""<p>The category for content filter evaluation.</p>"""
GuardrailChecksContentFilterCategory: TypeAlias = Literal[
    "VIOLENCE",
    "HATE",
    "SEXUAL",
    "MISCONDUCT",
    "INSULTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksContentFilterCategory) -> str:
    return value


def deserialize_json(data: str) -> GuardrailChecksContentFilterCategory:
    return cast(GuardrailChecksContentFilterCategory, data)
