"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupRecoveryPointDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_backup_recovery_point_calculated_lifecycle_details
    import capo_securityhub.types.aws_backup_recovery_point_created_by_details
    import capo_securityhub.types.aws_backup_recovery_point_lifecycle_details
    import capo_securityhub.types.boolean
    import capo_securityhub.types.long
    import capo_securityhub.types.non_empty_string


class AwsBackupRecoveryPointDetails(TypedDict, closed=True):
    backup_size_in_bytes: NotRequired["capo_securityhub.types.long.Long"]
    """<p>The size, in bytes, of a backup. </p>"""
    backup_vault_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a backup vault. </p>"""
    backup_vault_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the Amazon Web Services account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. </p>"""
    calculated_lifecycle: NotRequired[
        "capo_securityhub.types.aws_backup_recovery_point_calculated_lifecycle_details.AwsBackupRecoveryPointCalculatedLifecycleDetails"
    ]
    """<p>A <code>CalculatedLifecycle</code> object containing <code>DeleteAt</code> and <code>MoveToColdStorageAt</code> timestamps. </p>"""
    completion_date: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The date and time that a job to create a recovery point is completed, in Unix format and UTC. The value of <code>CompletionDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM. </p>"""
    created_by: NotRequired[
        "capo_securityhub.types.aws_backup_recovery_point_created_by_details.AwsBackupRecoveryPointCreatedByDetails"
    ]
    """<p>Contains identifying information about the creation of a recovery point, including the <code>BackupPlanArn</code>, <code>BackupPlanId</code>, <code>BackupPlanVersion</code>, and <code>BackupRuleId</code> of the backup plan that is used to create it. </p>"""
    creation_date: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The date and time a recovery point is created, in Unix format and UTC. The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM. </p>"""
    encryption_key_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN for the server-side encryption key that is used to protect your backups. </p>"""
    iam_role_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Specifies the IAM role ARN used to create the target recovery point </p>"""
    is_encrypted: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>A Boolean value that is returned as <code>TRUE</code> if the specified recovery point is encrypted, or <code>FALSE</code> if the recovery point is not encrypted. </p>"""
    last_restore_time: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The date and time that a recovery point was last restored, in Unix format and UTC. The value of <code>LastRestoreTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM. </p>"""
    lifecycle: NotRequired[
        "capo_securityhub.types.aws_backup_recovery_point_lifecycle_details.AwsBackupRecoveryPointLifecycleDetails"
    ]
    """<p>The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup transitions and expires backups automatically according to the lifecycle that you define </p>"""
    recovery_point_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>An ARN that uniquely identifies a recovery point. </p>"""
    resource_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type. </p>"""
    resource_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of Amazon Web Services resource saved as a recovery point, such as an Amazon EBS volume or an Amazon RDS database. </p>"""
    source_backup_vault_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN for the backup vault where the recovery point was originally copied from. If the recovery point is restored to the same account, this value will be null. </p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A status code specifying the state of the recovery point. Valid values are as follows:</p> <ul> <li> <p> <code>COMPLETED</code> </p> </li> <li> <p> <code>DELETING</code> </p> </li> <li> <p> <code>EXPIRED</code> </p> </li> <li> <p> <code>PARTIAL</code> </p> </li> </ul>"""
    status_message: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A message explaining the reason of the recovery point deletion failure. </p>"""
    storage_class: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Specifies the storage class of the recovery point. Valid values are as follows:</p> <ul> <li> <p> <code>COLD</code> </p> </li> <li> <p> <code>DELETED</code> </p> </li> <li> <p> <code>WARM</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupRecoveryPointDetails) -> dict:
    out: dict = {}
    if "backup_size_in_bytes" in value:
        out["BackupSizeInBytes"] = value["backup_size_in_bytes"]
    if "backup_vault_arn" in value:
        out["BackupVaultArn"] = value["backup_vault_arn"]
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    if "calculated_lifecycle" in value:
        import capo_securityhub.types.aws_backup_recovery_point_calculated_lifecycle_details

        out["CalculatedLifecycle"] = (
            capo_securityhub.types.aws_backup_recovery_point_calculated_lifecycle_details.serialize_json(
                value["calculated_lifecycle"]
            )
        )
    if "completion_date" in value:
        out["CompletionDate"] = value["completion_date"]
    if "created_by" in value:
        import capo_securityhub.types.aws_backup_recovery_point_created_by_details

        out["CreatedBy"] = (
            capo_securityhub.types.aws_backup_recovery_point_created_by_details.serialize_json(
                value["created_by"]
            )
        )
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "is_encrypted" in value:
        out["IsEncrypted"] = value["is_encrypted"]
    if "last_restore_time" in value:
        out["LastRestoreTime"] = value["last_restore_time"]
    if "lifecycle" in value:
        import capo_securityhub.types.aws_backup_recovery_point_lifecycle_details

        out["Lifecycle"] = (
            capo_securityhub.types.aws_backup_recovery_point_lifecycle_details.serialize_json(
                value["lifecycle"]
            )
        )
    if "recovery_point_arn" in value:
        out["RecoveryPointArn"] = value["recovery_point_arn"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "source_backup_vault_arn" in value:
        out["SourceBackupVaultArn"] = value["source_backup_vault_arn"]
    if "status" in value:
        out["Status"] = value["status"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "storage_class" in value:
        out["StorageClass"] = value["storage_class"]
    return out


def deserialize_json(data: dict) -> AwsBackupRecoveryPointDetails:
    out: AwsBackupRecoveryPointDetails = {}  # type: ignore[typeddict-item]
    if data.get("BackupSizeInBytes") is not None:
        out["backup_size_in_bytes"] = data["BackupSizeInBytes"]
    if data.get("BackupVaultArn") is not None:
        out["backup_vault_arn"] = data["BackupVaultArn"]
    if data.get("BackupVaultName") is not None:
        out["backup_vault_name"] = data["BackupVaultName"]
    if data.get("CalculatedLifecycle") is not None:
        import capo_securityhub.types.aws_backup_recovery_point_calculated_lifecycle_details

        out["calculated_lifecycle"] = (
            capo_securityhub.types.aws_backup_recovery_point_calculated_lifecycle_details.deserialize_json(
                data["CalculatedLifecycle"]
            )
        )
    if data.get("CompletionDate") is not None:
        out["completion_date"] = data["CompletionDate"]
    if data.get("CreatedBy") is not None:
        import capo_securityhub.types.aws_backup_recovery_point_created_by_details

        out["created_by"] = (
            capo_securityhub.types.aws_backup_recovery_point_created_by_details.deserialize_json(
                data["CreatedBy"]
            )
        )
    if data.get("CreationDate") is not None:
        out["creation_date"] = data["CreationDate"]
    if data.get("EncryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    if data.get("IsEncrypted") is not None:
        out["is_encrypted"] = data["IsEncrypted"]
    if data.get("LastRestoreTime") is not None:
        out["last_restore_time"] = data["LastRestoreTime"]
    if data.get("Lifecycle") is not None:
        import capo_securityhub.types.aws_backup_recovery_point_lifecycle_details

        out["lifecycle"] = (
            capo_securityhub.types.aws_backup_recovery_point_lifecycle_details.deserialize_json(
                data["Lifecycle"]
            )
        )
    if data.get("RecoveryPointArn") is not None:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("SourceBackupVaultArn") is not None:
        out["source_backup_vault_arn"] = data["SourceBackupVaultArn"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("StorageClass") is not None:
        out["storage_class"] = data["StorageClass"]
    return out
