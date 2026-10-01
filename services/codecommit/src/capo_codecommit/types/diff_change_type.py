"""Generated from Smithy shape ``com.amazonaws.codecommit#DiffChangeType``."""

from typing import Literal, TypeAlias, cast

DiffChangeType: TypeAlias = Literal[
    "CONTEXT",
    "ADD",
    "DELETE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiffChangeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DiffChangeType:
    return cast(DiffChangeType, data)
