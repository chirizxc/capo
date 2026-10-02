"""Generated from Smithy shape ``com.amazonaws.healthlake#ContinuousBackupRestoreConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.health_lake_timestamp


class ContinuousBackupRestoreConfiguration(TypedDict, closed=True):
    restore_point_time: NotRequired[
        "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
    ]
    """The point in time to restore the data store to, specified as a UTC timestamp."""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContinuousBackupRestoreConfiguration) -> dict:
    out: dict = {}
    if "restore_point_time" in value:
        import capo_healthlake.types.health_lake_timestamp

        out["RestorePointTime"] = (
            capo_healthlake.types.health_lake_timestamp.serialize_aws_json_1_0(
                value["restore_point_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ContinuousBackupRestoreConfiguration:
    out: ContinuousBackupRestoreConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RestorePointTime") is not None:
        import capo_healthlake.types.health_lake_timestamp

        out["restore_point_time"] = (
            capo_healthlake.types.health_lake_timestamp.deserialize_aws_json_1_0(
                data["RestorePointTime"]
            )
        )
    return out
