"""Generated from Smithy shape ``com.amazonaws.guardduty#ContentPolicyFilterType``."""

from typing import Literal, TypeAlias, cast

ContentPolicyFilterType: TypeAlias = Literal[
    "PROMPT_ATTACK",
    "JAILBREAK",
    "HATE",
    "INSULTS",
    "SEXUAL",
    "VIOLENCE",
    "MISCONDUCT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentPolicyFilterType) -> str:
    return value


def deserialize_json(data: str) -> ContentPolicyFilterType:
    return cast(ContentPolicyFilterType, data)
