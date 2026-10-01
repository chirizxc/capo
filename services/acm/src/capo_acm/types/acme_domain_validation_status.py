"""Generated from Smithy shape ``com.amazonaws.acm#AcmeDomainValidationStatus``."""

from typing import Literal, TypeAlias, cast

AcmeDomainValidationStatus: TypeAlias = Literal[
    "VALIDATING",
    "VALID",
    "INVALID",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmeDomainValidationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcmeDomainValidationStatus:
    return cast(AcmeDomainValidationStatus, data)
