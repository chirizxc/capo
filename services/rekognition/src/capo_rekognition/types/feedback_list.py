"""Generated from Smithy shape ``com.amazonaws.rekognition#FeedbackList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.feedback_item

FeedbackList: TypeAlias = list["capo_rekognition.types.feedback_item.FeedbackItem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeedbackList) -> list:
    import capo_rekognition.types.feedback_item

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.feedback_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FeedbackList:
    import capo_rekognition.types.feedback_item

    out: FeedbackList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_rekognition.types.feedback_item.deserialize_aws_json_1_1(item))
    return out
