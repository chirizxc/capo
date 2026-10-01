"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#StorageTier``."""

from typing import Literal, TypeAlias, cast

StorageTier: TypeAlias = Literal[
    "STANDARD",
    "INTELLIGENT_TIERING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageTier) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageTier:
    return cast(StorageTier, data)
