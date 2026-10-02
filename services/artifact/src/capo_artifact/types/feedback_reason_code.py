"""Generated from Smithy shape ``com.amazonaws.artifact#FeedbackReasonCode``."""

from typing import Literal, TypeAlias, cast

FeedbackReasonCode: TypeAlias = Literal[
    "OTHER",
    "PARTIAL_RESPONSE",
    "IRRELEVANT_RESPONSE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FeedbackReasonCode) -> str:
    return value


def deserialize_json(data: str) -> FeedbackReasonCode:
    return cast(FeedbackReasonCode, data)
