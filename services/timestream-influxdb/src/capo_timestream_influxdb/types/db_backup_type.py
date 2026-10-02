"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbBackupType``."""

from typing import Literal, TypeAlias, cast

DbBackupType: TypeAlias = Literal[
    "HOURLY",
    "DAILY",
    "WEEKLY",
    "MONTHLY",
    "CUSTOM_SCHEDULE",
    "ON_DEMAND",
    "CONTINUOUS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbBackupType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DbBackupType:
    return cast(DbBackupType, data)
