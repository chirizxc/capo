"""Generated from Smithy shape ``com.amazonaws.odb#UpdateAction``."""

from typing import Literal, TypeAlias, cast

UpdateAction: TypeAlias = Literal[
    "ROLLING_APPLY",
    "NON_ROLLING_APPLY",
    "PRECHECK",
    "ROLLBACK",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> UpdateAction:
    return cast(UpdateAction, data)
