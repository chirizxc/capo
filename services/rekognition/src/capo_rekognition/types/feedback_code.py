"""Generated from Smithy shape ``com.amazonaws.rekognition#FeedbackCode``."""

from typing import Literal, TypeAlias, cast

FeedbackCode: TypeAlias = Literal[
    "FACE_NOT_VISIBLE",
    "FACE_OBSTRUCTION_DETECTED",
    "LOW_VIDEO_QUALITY_DETECTED",
    "FACE_NOT_ALIGNED",
    "EYES_CLOSED_DETECTED",
    "LOW_LIGHTING_DETECTED",
    "HIGH_LIGHTING_DETECTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeedbackCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeedbackCode:
    return cast(FeedbackCode, data)
