"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#ExtractedInformationFailureCode``."""

from typing import Literal, TypeAlias, cast

ExtractedInformationFailureCode: TypeAlias = Literal[
    "QUOTA_EXCEEDED",
    "INSUFFICIENT_CONVERSATION_CONTENT",
    "FAILED_SAFETY_GUIDELINES",
    "INTERNAL_ERROR",
    "MAX_PACKAGE_FEATURE_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExtractedInformationFailureCode) -> str:
    return value


def deserialize_json(data: str) -> ExtractedInformationFailureCode:
    return cast(ExtractedInformationFailureCode, data)
