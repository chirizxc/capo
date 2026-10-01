"""Generated from Smithy shape ``com.amazonaws.artifact#InquiryStatus``."""

from typing import Literal, TypeAlias, cast

InquiryStatus: TypeAlias = Literal[
    "PROCESSING",
    "HUMAN_REVIEW",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InquiryStatus) -> str:
    return value


def deserialize_json(data: str) -> InquiryStatus:
    return cast(InquiryStatus, data)
