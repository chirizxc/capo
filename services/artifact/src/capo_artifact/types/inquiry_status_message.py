"""Generated from Smithy shape ``com.amazonaws.artifact#InquiryStatusMessage``."""

from typing import Literal, TypeAlias, cast

InquiryStatusMessage: TypeAlias = Literal[
    "Compliance inquiry processing is complete.",
    "Malware was detected on the file. Provide a new file and try again.",
    "Compliance inquiry processing is in-progress.",
    "An internal error occurred while processing the inquiry. Try again at a later time.",
    "Human review is in progress.",
    "Compliance inquiry processing is complete. One or more queries encountered errors during processing.",
]


# --- restJson1 ser/de ---
def serialize_json(value: InquiryStatusMessage) -> str:
    return value


def deserialize_json(data: str) -> InquiryStatusMessage:
    return cast(InquiryStatusMessage, data)
