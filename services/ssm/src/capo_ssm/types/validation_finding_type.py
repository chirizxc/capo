"""Generated from Smithy shape ``com.amazonaws.ssm#ValidationFindingType``."""

from typing import Literal, TypeAlias, cast

ValidationFindingType: TypeAlias = Literal[
    "INFO",
    "WARN",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationFindingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValidationFindingType:
    return cast(ValidationFindingType, data)
