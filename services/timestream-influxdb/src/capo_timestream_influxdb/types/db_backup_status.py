"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbBackupStatus``."""

from typing import Literal, TypeAlias, cast

DbBackupStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "DELETING",
    "DELETED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbBackupStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DbBackupStatus:
    return cast(DbBackupStatus, data)
