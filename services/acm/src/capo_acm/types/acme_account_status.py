"""Generated from Smithy shape ``com.amazonaws.acm#AcmeAccountStatus``."""

from typing import Literal, TypeAlias, cast

AcmeAccountStatus: TypeAlias = Literal[
    "VALID",
    "DEACTIVATED",
    "REVOKED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmeAccountStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcmeAccountStatus:
    return cast(AcmeAccountStatus, data)
