"""Generated from Smithy shape ``com.amazonaws.healthlake#BackupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.backup_retention_period_in_days
    import capo_healthlake.types.backup_status
    import capo_healthlake.types.backup_type
    import capo_healthlake.types.health_lake_boolean


class BackupConfiguration(TypedDict, closed=True):
    status: NotRequired["capo_healthlake.types.backup_status.BackupStatus"]
    """The backup status of the data store."""
    backup_type: NotRequired["capo_healthlake.types.backup_type.BackupType"]
    """The type of backup."""
    retention_period_in_days: NotRequired[
        "capo_healthlake.types.backup_retention_period_in_days.BackupRetentionPeriodInDays"
    ]
    """The number of days backup data is retained."""
    backup_tags_enabled: "capo_healthlake.types.health_lake_boolean.HealthLakeBoolean"
    """Specifies whether tags are included in backups."""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BackupConfiguration) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_healthlake.types.backup_status

        out["Status"] = capo_healthlake.types.backup_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "backup_type" in value:
        import capo_healthlake.types.backup_type

        out["BackupType"] = capo_healthlake.types.backup_type.serialize_aws_json_1_0(
            value["backup_type"]
        )
    if "retention_period_in_days" in value:
        out["RetentionPeriodInDays"] = value["retention_period_in_days"]
    out["BackupTagsEnabled"] = value.get("backup_tags_enabled", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> BackupConfiguration:
    out: BackupConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_healthlake.types.backup_status

        out["status"] = capo_healthlake.types.backup_status.deserialize_aws_json_1_0(
            data["Status"]
        )
    if data.get("BackupType") is not None:
        import capo_healthlake.types.backup_type

        out["backup_type"] = capo_healthlake.types.backup_type.deserialize_aws_json_1_0(
            data["BackupType"]
        )
    if data.get("RetentionPeriodInDays") is not None:
        out["retention_period_in_days"] = data["RetentionPeriodInDays"]
    if data.get("BackupTagsEnabled") is not None:
        out["backup_tags_enabled"] = data["BackupTagsEnabled"]
    else:
        out["backup_tags_enabled"] = False
    return out
