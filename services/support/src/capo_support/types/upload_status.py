"""Generated from Smithy shape ``com.amazonaws.support#UploadStatus``."""

from typing import Literal, TypeAlias, cast

UploadStatus: TypeAlias = Literal[
    "attachment-ready",
    "attachment-not-ready",
    "failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UploadStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UploadStatus:
    return cast(UploadStatus, data)
