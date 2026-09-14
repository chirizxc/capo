"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#Snapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_redshift_serverless.types.account_id_list
    import capo_redshift_serverless.types.kms_key_id
    import capo_redshift_serverless.types.snapshot_status


class Snapshot(TypedDict, closed=True):
    namespace_name: NotRequired["str"]
    """<p>The name of the namepsace.</p>"""
    namespace_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the namespace the snapshot was created from.</p>"""
    snapshot_name: NotRequired["str"]
    """<p>The name of the snapshot.</p>"""
    snapshot_create_time: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the snapshot was created.</p>"""
    admin_username: NotRequired["str"]
    """<p>The username of the database within a snapshot.</p>"""
    status: NotRequired["capo_redshift_serverless.types.snapshot_status.SnapshotStatus"]
    """<p>The status of the snapshot.</p>"""
    kms_key_id: NotRequired["capo_redshift_serverless.types.kms_key_id.KmsKeyId"]
    """<p>The unique identifier of the KMS key used to encrypt the snapshot.</p>"""
    owner_account: NotRequired["str"]
    """<p>The owner Amazon Web Services; account of the snapshot.</p>"""
    total_backup_size_in_mega_bytes: NotRequired["float"]
    """<p>The total size, in megabytes, of how big the snapshot is.</p>"""
    actual_incremental_backup_size_in_mega_bytes: NotRequired["float"]
    """<p>The size of the incremental backup in megabytes.</p>"""
    backup_progress_in_mega_bytes: NotRequired["float"]
    """<p>The size in megabytes of the data that has been backed up to a snapshot.</p>"""
    current_backup_rate_in_mega_bytes_per_second: NotRequired["float"]
    """<p>The rate at which data is backed up into a snapshot in megabytes per second.</p>"""
    estimated_seconds_to_completion: NotRequired["int"]
    """<p>The estimated amount of seconds until the snapshot completes backup.</p>"""
    elapsed_time_in_seconds: NotRequired["int"]
    """<p>The amount of time it took to back up data into a snapshot.</p>"""
    snapshot_retention_period: NotRequired["int"]
    """<p>The period of time, in days, of how long the snapshot is retained.</p>"""
    snapshot_remaining_days: NotRequired["int"]
    """<p>The amount of days until the snapshot is deleted.</p>"""
    snapshot_retention_start_time: NotRequired["datetime.datetime"]
    """<p>The timestamp of when data within the snapshot started getting retained.</p>"""
    snapshot_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the snapshot.</p>"""
    accounts_with_restore_access: NotRequired[
        "capo_redshift_serverless.types.account_id_list.AccountIdList"
    ]
    """<p>All of the Amazon Web Services accounts that have access to restore a snapshot to a namespace.</p>"""
    accounts_with_provisioned_restore_access: NotRequired[
        "capo_redshift_serverless.types.account_id_list.AccountIdList"
    ]
    """<p>All of the Amazon Web Services accounts that have access to restore a snapshot to a provisioned cluster.</p>"""
    admin_password_secret_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) for the namespace's admin user credentials secret.</p>"""
    admin_password_secret_kms_key_id: NotRequired[
        "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
    ]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Snapshot) -> dict:
    out: dict = {}
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "namespace_arn" in value:
        out["namespaceArn"] = value["namespace_arn"]
    if "snapshot_name" in value:
        out["snapshotName"] = value["snapshot_name"]
    if "snapshot_create_time" in value:
        import capo_redshift_serverless._protocol.serialize

        out["snapshotCreateTime"] = (
            capo_redshift_serverless._protocol.serialize.fmt_date_time(
                value["snapshot_create_time"]
            )
        )
    if "admin_username" in value:
        out["adminUsername"] = value["admin_username"]
    if "status" in value:
        out["status"] = value["status"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "total_backup_size_in_mega_bytes" in value:
        out["totalBackupSizeInMegaBytes"] = (
            "NaN"
            if value["total_backup_size_in_mega_bytes"]
            != value["total_backup_size_in_mega_bytes"]
            else "Infinity"
            if value["total_backup_size_in_mega_bytes"] == float("inf")
            else "-Infinity"
            if value["total_backup_size_in_mega_bytes"] == float("-inf")
            else value["total_backup_size_in_mega_bytes"]
        )
    if "actual_incremental_backup_size_in_mega_bytes" in value:
        out["actualIncrementalBackupSizeInMegaBytes"] = (
            "NaN"
            if value["actual_incremental_backup_size_in_mega_bytes"]
            != value["actual_incremental_backup_size_in_mega_bytes"]
            else "Infinity"
            if value["actual_incremental_backup_size_in_mega_bytes"] == float("inf")
            else "-Infinity"
            if value["actual_incremental_backup_size_in_mega_bytes"] == float("-inf")
            else value["actual_incremental_backup_size_in_mega_bytes"]
        )
    if "backup_progress_in_mega_bytes" in value:
        out["backupProgressInMegaBytes"] = (
            "NaN"
            if value["backup_progress_in_mega_bytes"]
            != value["backup_progress_in_mega_bytes"]
            else "Infinity"
            if value["backup_progress_in_mega_bytes"] == float("inf")
            else "-Infinity"
            if value["backup_progress_in_mega_bytes"] == float("-inf")
            else value["backup_progress_in_mega_bytes"]
        )
    if "current_backup_rate_in_mega_bytes_per_second" in value:
        out["currentBackupRateInMegaBytesPerSecond"] = (
            "NaN"
            if value["current_backup_rate_in_mega_bytes_per_second"]
            != value["current_backup_rate_in_mega_bytes_per_second"]
            else "Infinity"
            if value["current_backup_rate_in_mega_bytes_per_second"] == float("inf")
            else "-Infinity"
            if value["current_backup_rate_in_mega_bytes_per_second"] == float("-inf")
            else value["current_backup_rate_in_mega_bytes_per_second"]
        )
    if "estimated_seconds_to_completion" in value:
        out["estimatedSecondsToCompletion"] = value["estimated_seconds_to_completion"]
    if "elapsed_time_in_seconds" in value:
        out["elapsedTimeInSeconds"] = value["elapsed_time_in_seconds"]
    if "snapshot_retention_period" in value:
        out["snapshotRetentionPeriod"] = value["snapshot_retention_period"]
    if "snapshot_remaining_days" in value:
        out["snapshotRemainingDays"] = value["snapshot_remaining_days"]
    if "snapshot_retention_start_time" in value:
        import capo_redshift_serverless._protocol.serialize

        out["snapshotRetentionStartTime"] = (
            capo_redshift_serverless._protocol.serialize.fmt_date_time(
                value["snapshot_retention_start_time"]
            )
        )
    if "snapshot_arn" in value:
        out["snapshotArn"] = value["snapshot_arn"]
    if "accounts_with_restore_access" in value:
        import capo_redshift_serverless.types.account_id_list

        out["accountsWithRestoreAccess"] = (
            capo_redshift_serverless.types.account_id_list.serialize_aws_json_1_1(
                value["accounts_with_restore_access"]
            )
        )
    if "accounts_with_provisioned_restore_access" in value:
        import capo_redshift_serverless.types.account_id_list

        out["accountsWithProvisionedRestoreAccess"] = (
            capo_redshift_serverless.types.account_id_list.serialize_aws_json_1_1(
                value["accounts_with_provisioned_restore_access"]
            )
        )
    if "admin_password_secret_arn" in value:
        out["adminPasswordSecretArn"] = value["admin_password_secret_arn"]
    if "admin_password_secret_kms_key_id" in value:
        out["adminPasswordSecretKmsKeyId"] = value["admin_password_secret_kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Snapshot:
    out: Snapshot = {}  # type: ignore[typeddict-item]
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    if data.get("namespaceArn") is not None:
        out["namespace_arn"] = data["namespaceArn"]
    if data.get("snapshotName") is not None:
        out["snapshot_name"] = data["snapshotName"]
    if data.get("snapshotCreateTime") is not None:
        import datetime

        out["snapshot_create_time"] = datetime.datetime.fromisoformat(
            data["snapshotCreateTime"].replace("Z", "+00:00")
        )
    if data.get("adminUsername") is not None:
        out["admin_username"] = data["adminUsername"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    if data.get("totalBackupSizeInMegaBytes") is not None:
        out["total_backup_size_in_mega_bytes"] = float(
            data["totalBackupSizeInMegaBytes"]
        )
    if data.get("actualIncrementalBackupSizeInMegaBytes") is not None:
        out["actual_incremental_backup_size_in_mega_bytes"] = float(
            data["actualIncrementalBackupSizeInMegaBytes"]
        )
    if data.get("backupProgressInMegaBytes") is not None:
        out["backup_progress_in_mega_bytes"] = float(data["backupProgressInMegaBytes"])
    if data.get("currentBackupRateInMegaBytesPerSecond") is not None:
        out["current_backup_rate_in_mega_bytes_per_second"] = float(
            data["currentBackupRateInMegaBytesPerSecond"]
        )
    if data.get("estimatedSecondsToCompletion") is not None:
        out["estimated_seconds_to_completion"] = data["estimatedSecondsToCompletion"]
    if data.get("elapsedTimeInSeconds") is not None:
        out["elapsed_time_in_seconds"] = data["elapsedTimeInSeconds"]
    if data.get("snapshotRetentionPeriod") is not None:
        out["snapshot_retention_period"] = data["snapshotRetentionPeriod"]
    if data.get("snapshotRemainingDays") is not None:
        out["snapshot_remaining_days"] = data["snapshotRemainingDays"]
    if data.get("snapshotRetentionStartTime") is not None:
        import datetime

        out["snapshot_retention_start_time"] = datetime.datetime.fromisoformat(
            data["snapshotRetentionStartTime"].replace("Z", "+00:00")
        )
    if data.get("snapshotArn") is not None:
        out["snapshot_arn"] = data["snapshotArn"]
    if data.get("accountsWithRestoreAccess") is not None:
        import capo_redshift_serverless.types.account_id_list

        out["accounts_with_restore_access"] = (
            capo_redshift_serverless.types.account_id_list.deserialize_aws_json_1_1(
                data["accountsWithRestoreAccess"]
            )
        )
    if data.get("accountsWithProvisionedRestoreAccess") is not None:
        import capo_redshift_serverless.types.account_id_list

        out["accounts_with_provisioned_restore_access"] = (
            capo_redshift_serverless.types.account_id_list.deserialize_aws_json_1_1(
                data["accountsWithProvisionedRestoreAccess"]
            )
        )
    if data.get("adminPasswordSecretArn") is not None:
        out["admin_password_secret_arn"] = data["adminPasswordSecretArn"]
    if data.get("adminPasswordSecretKmsKeyId") is not None:
        out["admin_password_secret_kms_key_id"] = data["adminPasswordSecretKmsKeyId"]
    return out
