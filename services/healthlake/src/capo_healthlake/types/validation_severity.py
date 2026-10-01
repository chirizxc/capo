"""Generated from Smithy shape ``com.amazon.awshealthlakedatatransformationfrontendservice#ValidationSeverity``."""

from typing import Literal, TypeAlias, cast

ValidationSeverity: TypeAlias = Literal[
    "ERROR",
    "WARNING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationSeverity) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationSeverity:
    return cast(ValidationSeverity, data)
