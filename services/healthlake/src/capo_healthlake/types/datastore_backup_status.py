"""Generated from Smithy shape ``com.amazonaws.healthlake#DatastoreBackupStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.backup_configuration
    import capo_healthlake.types.health_lake_timestamp


class DatastoreBackupStatus(TypedDict, closed=True):
    configuration: NotRequired[
        "capo_healthlake.types.backup_configuration.BackupConfiguration"
    ]
    """The backup configuration for the data store."""
    backup_enabled_at: NotRequired[
        "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
    ]
    """The time backup was enabled on the data store."""
    earliest_restore_point: NotRequired[
        "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
    ]
    """The earliest point in time the data store can be restored to."""
    latest_restore_point: NotRequired[
        "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
    ]
    """The latest point in time the data store can be restored to."""
    scheduled_permanent_deletion_time: NotRequired[
        "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
    ]
    """The time the retained backup data is scheduled for permanent deletion."""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatastoreBackupStatus) -> dict:
    out: dict = {}
    if "configuration" in value:
        import capo_healthlake.types.backup_configuration

        out["Configuration"] = (
            capo_healthlake.types.backup_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    if "backup_enabled_at" in value:
        import capo_healthlake.types.health_lake_timestamp

        out["BackupEnabledAt"] = (
            capo_healthlake.types.health_lake_timestamp.serialize_aws_json_1_0(
                value["backup_enabled_at"]
            )
        )
    if "earliest_restore_point" in value:
        import capo_healthlake.types.health_lake_timestamp

        out["EarliestRestorePoint"] = (
            capo_healthlake.types.health_lake_timestamp.serialize_aws_json_1_0(
                value["earliest_restore_point"]
            )
        )
    if "latest_restore_point" in value:
        import capo_healthlake.types.health_lake_timestamp

        out["LatestRestorePoint"] = (
            capo_healthlake.types.health_lake_timestamp.serialize_aws_json_1_0(
                value["latest_restore_point"]
            )
        )
    if "scheduled_permanent_deletion_time" in value:
        import capo_healthlake.types.health_lake_timestamp

        out["ScheduledPermanentDeletionTime"] = (
            capo_healthlake.types.health_lake_timestamp.serialize_aws_json_1_0(
                value["scheduled_permanent_deletion_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DatastoreBackupStatus:
    out: DatastoreBackupStatus = {}  # type: ignore[typeddict-item]
    if data.get("Configuration") is not None:
        import capo_healthlake.types.backup_configuration

        out["configuration"] = (
            capo_healthlake.types.backup_configuration.deserialize_aws_json_1_0(
                data["Configuration"]
            )
        )
    if data.get("BackupEnabledAt") is not None:
        import capo_healthlake.types.health_lake_timestamp

        out["backup_enabled_at"] = (
            capo_healthlake.types.health_lake_timestamp.deserialize_aws_json_1_0(
                data["BackupEnabledAt"]
            )
        )
    if data.get("EarliestRestorePoint") is not None:
        import capo_healthlake.types.health_lake_timestamp

        out["earliest_restore_point"] = (
            capo_healthlake.types.health_lake_timestamp.deserialize_aws_json_1_0(
                data["EarliestRestorePoint"]
            )
        )
    if data.get("LatestRestorePoint") is not None:
        import capo_healthlake.types.health_lake_timestamp

        out["latest_restore_point"] = (
            capo_healthlake.types.health_lake_timestamp.deserialize_aws_json_1_0(
                data["LatestRestorePoint"]
            )
        )
    if data.get("ScheduledPermanentDeletionTime") is not None:
        import capo_healthlake.types.health_lake_timestamp

        out["scheduled_permanent_deletion_time"] = (
            capo_healthlake.types.health_lake_timestamp.deserialize_aws_json_1_0(
                data["ScheduledPermanentDeletionTime"]
            )
        )
    return out
