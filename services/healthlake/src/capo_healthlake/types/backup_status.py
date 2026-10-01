"""Generated from Smithy shape ``com.amazonaws.healthlake#BackupStatus``."""

from typing import Literal, TypeAlias, cast

BackupStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BackupStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BackupStatus:
    return cast(BackupStatus, data)
