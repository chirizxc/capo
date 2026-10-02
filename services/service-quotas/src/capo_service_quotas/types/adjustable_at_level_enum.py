"""Generated from Smithy shape ``com.amazonaws.servicequotas#AdjustableAtLevelEnum``."""

from typing import Literal, TypeAlias, cast

AdjustableAtLevelEnum: TypeAlias = Literal[
    "ACCOUNT",
    "PER_RESOURCE",
    "ALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdjustableAtLevelEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdjustableAtLevelEnum:
    return cast(AdjustableAtLevelEnum, data)
