"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseBackupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_odb.types.autonomous_database_backup_status
    import capo_odb.types.autonomous_database_backup_type
    import capo_odb.types.resource_arn
    import capo_odb.types.resource_id


class AutonomousDatabaseBackupSummary(TypedDict, closed=True):
    autonomous_database_backup_id: NotRequired["capo_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the Autonomous Database backup.</p>"""
    autonomous_database_backup_arn: NotRequired[
        "capo_odb.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Autonomous Database backup.</p>"""
    autonomous_database_id: NotRequired["capo_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the Autonomous Database that the backup was created from.</p>"""
    ocid: NotRequired["str"]
    """<p>The Oracle Cloud Identifier (OCID) of the Autonomous Database backup.</p>"""
    display_name: NotRequired["str"]
    """<p>The user-friendly name of the Autonomous Database backup.</p>"""
    db_version: NotRequired["str"]
    """<p>The Oracle Database software version of the Autonomous Database backup.</p>"""
    status: NotRequired[
        "capo_odb.types.autonomous_database_backup_status.AutonomousDatabaseBackupStatus"
    ]
    """<p>The current status of the Autonomous Database backup.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the Autonomous Database backup, if applicable.</p>"""
    is_automatic: NotRequired["bool"]
    """<p>Indicates whether the backup was created automatically.</p>"""
    retention_period_in_days: NotRequired["int"]
    """<p>The retention period, in days, for the Autonomous Database backup.</p>"""
    size_in_t_bs: NotRequired["float"]
    """<p>The size of the Autonomous Database backup, in terabytes (TB).</p>"""
    time_available_till: NotRequired["datetime.datetime"]
    """<p>The date and time until which the Autonomous Database backup is available for restore.</p>"""
    time_started: NotRequired["datetime.datetime"]
    """<p>The date and time when the Autonomous Database backup started.</p>"""
    time_ended: NotRequired["datetime.datetime"]
    """<p>The date and time when the Autonomous Database backup ended.</p>"""
    type: NotRequired[
        "capo_odb.types.autonomous_database_backup_type.AutonomousDatabaseBackupType"
    ]
    """<p>The type of the Autonomous Database backup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseBackupSummary) -> dict:
    out: dict = {}
    if "autonomous_database_backup_id" in value:
        out["autonomousDatabaseBackupId"] = value["autonomous_database_backup_id"]
    if "autonomous_database_backup_arn" in value:
        out["autonomousDatabaseBackupArn"] = value["autonomous_database_backup_arn"]
    if "autonomous_database_id" in value:
        out["autonomousDatabaseId"] = value["autonomous_database_id"]
    if "ocid" in value:
        out["ocid"] = value["ocid"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "db_version" in value:
        out["dbVersion"] = value["db_version"]
    if "status" in value:
        import capo_odb.types.autonomous_database_backup_status

        out["status"] = (
            capo_odb.types.autonomous_database_backup_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "is_automatic" in value:
        out["isAutomatic"] = value["is_automatic"]
    if "retention_period_in_days" in value:
        out["retentionPeriodInDays"] = value["retention_period_in_days"]
    if "size_in_t_bs" in value:
        out["sizeInTBs"] = (
            "NaN"
            if value["size_in_t_bs"] != value["size_in_t_bs"]
            else "Infinity"
            if value["size_in_t_bs"] == float("inf")
            else "-Infinity"
            if value["size_in_t_bs"] == float("-inf")
            else value["size_in_t_bs"]
        )
    if "time_available_till" in value:
        import capo_odb._protocol.serialize

        out["timeAvailableTill"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_available_till"]
        )
    if "time_started" in value:
        import capo_odb._protocol.serialize

        out["timeStarted"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_started"]
        )
    if "time_ended" in value:
        import capo_odb._protocol.serialize

        out["timeEnded"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_ended"]
        )
    if "type" in value:
        import capo_odb.types.autonomous_database_backup_type

        out["type"] = (
            capo_odb.types.autonomous_database_backup_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutonomousDatabaseBackupSummary:
    out: AutonomousDatabaseBackupSummary = {}  # type: ignore[typeddict-item]
    if data.get("autonomousDatabaseBackupId") is not None:
        out["autonomous_database_backup_id"] = data["autonomousDatabaseBackupId"]
    if data.get("autonomousDatabaseBackupArn") is not None:
        out["autonomous_database_backup_arn"] = data["autonomousDatabaseBackupArn"]
    if data.get("autonomousDatabaseId") is not None:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    if data.get("ocid") is not None:
        out["ocid"] = data["ocid"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("dbVersion") is not None:
        out["db_version"] = data["dbVersion"]
    if data.get("status") is not None:
        import capo_odb.types.autonomous_database_backup_status

        out["status"] = (
            capo_odb.types.autonomous_database_backup_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("isAutomatic") is not None:
        out["is_automatic"] = data["isAutomatic"]
    if data.get("retentionPeriodInDays") is not None:
        out["retention_period_in_days"] = data["retentionPeriodInDays"]
    if data.get("sizeInTBs") is not None:
        out["size_in_t_bs"] = float(data["sizeInTBs"])
    if data.get("timeAvailableTill") is not None:
        import datetime

        out["time_available_till"] = datetime.datetime.fromisoformat(
            data["timeAvailableTill"].replace("Z", "+00:00")
        )
    if data.get("timeStarted") is not None:
        import datetime

        out["time_started"] = datetime.datetime.fromisoformat(
            data["timeStarted"].replace("Z", "+00:00")
        )
    if data.get("timeEnded") is not None:
        import datetime

        out["time_ended"] = datetime.datetime.fromisoformat(
            data["timeEnded"].replace("Z", "+00:00")
        )
    if data.get("type") is not None:
        import capo_odb.types.autonomous_database_backup_type

        out["type"] = (
            capo_odb.types.autonomous_database_backup_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    return out
