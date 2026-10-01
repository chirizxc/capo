"""Generated from Smithy shape ``com.amazonaws.artifact#FeedbackReasonCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_artifact.types.feedback_reason_code

FeedbackReasonCodeList: TypeAlias = list[
    "capo_artifact.types.feedback_reason_code.FeedbackReasonCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: FeedbackReasonCodeList) -> list:
    import capo_artifact.types.feedback_reason_code

    out: list = []
    for item in value:
        out.append(capo_artifact.types.feedback_reason_code.serialize_json(item))
    return out


def deserialize_json(data: list) -> FeedbackReasonCodeList:
    import capo_artifact.types.feedback_reason_code

    out: FeedbackReasonCodeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_artifact.types.feedback_reason_code.deserialize_json(item))
    return out
