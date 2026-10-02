"""Generated from Smithy shape ``com.amazonaws.guardduty#GuardrailSource``."""

from typing import Literal, TypeAlias, cast

GuardrailSource: TypeAlias = Literal[
    "INPUT",
    "OUTPUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailSource) -> str:
    return value


def deserialize_json(data: str) -> GuardrailSource:
    return cast(GuardrailSource, data)
