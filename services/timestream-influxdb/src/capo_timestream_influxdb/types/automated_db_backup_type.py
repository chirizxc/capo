"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#AutomatedDbBackupType``."""

from typing import Literal, TypeAlias, cast

AutomatedDbBackupType: TypeAlias = Literal[
    "HOURLY",
    "DAILY",
    "WEEKLY",
    "MONTHLY",
    "CUSTOM_SCHEDULE",
    "CONTINUOUS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutomatedDbBackupType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutomatedDbBackupType:
    return cast(AutomatedDbBackupType, data)
