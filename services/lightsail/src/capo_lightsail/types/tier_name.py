"""Generated from Smithy shape ``com.amazonaws.lightsail#TierName``."""

from typing import Literal, TypeAlias, cast

TierName: TypeAlias = Literal[
    "Essential",
    "Growth",
    "Accelerate",
    "Premier",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TierName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TierName:
    return cast(TierName, data)
