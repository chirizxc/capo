"""Generated from Smithy shape ``com.amazonaws.acm#AcmeAuthorizationBehavior``."""

from typing import Literal, TypeAlias, cast

AcmeAuthorizationBehavior: TypeAlias = Literal["PRE_APPROVED",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmeAuthorizationBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcmeAuthorizationBehavior:
    return cast(AcmeAuthorizationBehavior, data)
