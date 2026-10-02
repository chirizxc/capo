"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SecurityPolicyType``."""

from typing import Literal, TypeAlias, cast

SecurityPolicyType: TypeAlias = Literal[
    "TLS_V1",
    "TLS_V1_2_2021",
    "TLS_V1_3_2025",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityPolicyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SecurityPolicyType:
    return cast(SecurityPolicyType, data)
