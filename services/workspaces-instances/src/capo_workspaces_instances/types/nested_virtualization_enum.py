"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#NestedVirtualizationEnum``."""

from typing import Literal, TypeAlias, cast

NestedVirtualizationEnum: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NestedVirtualizationEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NestedVirtualizationEnum:
    return cast(NestedVirtualizationEnum, data)
