"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#RestoreMode``."""

from typing import Literal, TypeAlias, cast

RestoreMode: TypeAlias = Literal[
    "NEW_RESOURCE",
    "REPLACE_EXISTING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RestoreMode:
    return cast(RestoreMode, data)
