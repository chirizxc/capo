"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressCpuArchitecture``."""

from typing import Literal, TypeAlias, cast

ExpressCpuArchitecture: TypeAlias = Literal[
    "X86_64",
    "ARM64",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressCpuArchitecture) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExpressCpuArchitecture:
    return cast(ExpressCpuArchitecture, data)
