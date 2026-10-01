"""Generated from Smithy shape ``com.amazonaws.acm#AcmeEndpointStatus``."""

from typing import Literal, TypeAlias, cast

AcmeEndpointStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmeEndpointStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcmeEndpointStatus:
    return cast(AcmeEndpointStatus, data)
