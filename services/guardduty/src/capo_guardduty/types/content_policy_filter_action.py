"""Generated from Smithy shape ``com.amazonaws.guardduty#ContentPolicyFilterAction``."""

from typing import Literal, TypeAlias, cast

ContentPolicyFilterAction: TypeAlias = Literal[
    "BLOCKED",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentPolicyFilterAction) -> str:
    return value


def deserialize_json(data: str) -> ContentPolicyFilterAction:
    return cast(ContentPolicyFilterAction, data)
