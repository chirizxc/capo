"""Generated from Smithy shape ``com.amazonaws.healthlake#RestoreConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_healthlake.types.continuous_backup_restore_configuration


class _RestoreConfiguration_ContinuousBackupRestoreConfiguration(
    TypedDict, closed=True
):
    ContinuousBackupRestoreConfiguration: "capo_healthlake.types.continuous_backup_restore_configuration.ContinuousBackupRestoreConfiguration"


RestoreConfiguration: TypeAlias = (
    _RestoreConfiguration_ContinuousBackupRestoreConfiguration
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreConfiguration) -> dict:
    if "ContinuousBackupRestoreConfiguration" in value:
        import capo_healthlake.types.continuous_backup_restore_configuration

        return {
            "ContinuousBackupRestoreConfiguration": capo_healthlake.types.continuous_backup_restore_configuration.serialize_aws_json_1_0(
                value["ContinuousBackupRestoreConfiguration"]
            )
        }
    else:
        raise SerializationError("RestoreConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RestoreConfiguration:
    if data.get("ContinuousBackupRestoreConfiguration") is not None:
        import capo_healthlake.types.continuous_backup_restore_configuration

        return {
            "ContinuousBackupRestoreConfiguration": capo_healthlake.types.continuous_backup_restore_configuration.deserialize_aws_json_1_0(
                data["ContinuousBackupRestoreConfiguration"]
            )
        }
    else:
        raise DeserializationError("RestoreConfiguration: no recognized variant key")
