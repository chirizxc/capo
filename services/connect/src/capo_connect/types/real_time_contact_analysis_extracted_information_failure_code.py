"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisExtractedInformationFailureCode``."""

from typing import Literal, TypeAlias, cast

RealTimeContactAnalysisExtractedInformationFailureCode: TypeAlias = Literal[
    "QUOTA_EXCEEDED",
    "INSUFFICIENT_CONVERSATION_CONTENT",
    "FAILED_SAFETY_GUIDELINES",
    "INTERNAL_ERROR",
    "MAX_PACKAGE_FEATURE_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(
    value: RealTimeContactAnalysisExtractedInformationFailureCode,
) -> str:
    return value


def deserialize_json(
    data: str,
) -> RealTimeContactAnalysisExtractedInformationFailureCode:
    return cast(RealTimeContactAnalysisExtractedInformationFailureCode, data)
