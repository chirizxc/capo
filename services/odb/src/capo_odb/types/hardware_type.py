"""Generated from Smithy shape ``com.amazonaws.odb#HardwareType``."""

from typing import Literal, TypeAlias, cast

HardwareType: TypeAlias = Literal[
    "COMPUTE",
    "CELL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HardwareType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HardwareType:
    return cast(HardwareType, data)
