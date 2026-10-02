"""Generated from Smithy shape ``com.amazonaws.healthlake#BackupType``."""

from typing import Literal, TypeAlias, cast

BackupType: TypeAlias = Literal["CONTINUOUS",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BackupType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BackupType:
    return cast(BackupType, data)
