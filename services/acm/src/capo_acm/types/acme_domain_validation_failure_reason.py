"""Generated from Smithy shape ``com.amazonaws.acm#AcmeDomainValidationFailureReason``."""

from typing import Literal, TypeAlias, cast

AcmeDomainValidationFailureReason: TypeAlias = Literal[
    "ACCESS_DENIED",
    "DOMAIN_MISMATCH",
    "DOMAIN_NOT_ALLOWED",
    "ENDPOINT_NOT_ACTIVE",
    "HOSTED_ZONE_NOT_FOUND",
    "INTERNAL_FAILURE",
    "INVALID_CHANGE_BATCH",
    "INVALID_PUBLIC_DOMAIN",
    "TIMED_OUT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmeDomainValidationFailureReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcmeDomainValidationFailureReason:
    return cast(AcmeDomainValidationFailureReason, data)
