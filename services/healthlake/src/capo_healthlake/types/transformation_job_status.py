"""Generated from Smithy shape ``com.amazonaws.healthlake#TransformationJobStatus``."""

from typing import Literal, TypeAlias, cast

TransformationJobStatus: TypeAlias = Literal[
    "SUBMITTED",
    "QUEUED",
    "IN_PROGRESS",
    "COMPLETED",
    "COMPLETED_WITH_ERRORS",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransformationJobStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TransformationJobStatus:
    return cast(TransformationJobStatus, data)
