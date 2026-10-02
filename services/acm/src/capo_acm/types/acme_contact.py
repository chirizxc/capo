"""Generated from Smithy shape ``com.amazonaws.acm#AcmeContact``."""

from typing import Literal, TypeAlias, cast

AcmeContact: TypeAlias = Literal[
    "REQUIRED",
    "NOT_REQUIRED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmeContact) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcmeContact:
    return cast(AcmeContact, data)
