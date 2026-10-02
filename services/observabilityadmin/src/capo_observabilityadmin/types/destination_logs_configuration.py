"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#DestinationLogsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.log_group_name_configuration
    import capo_observabilityadmin.types.logs_backup_configuration
    import capo_observabilityadmin.types.logs_encryption_configuration
    import capo_observabilityadmin.types.tag_propagation_configuration


class DestinationLogsConfiguration(TypedDict, closed=True):
    logs_encryption_configuration: NotRequired[
        "capo_observabilityadmin.types.logs_encryption_configuration.LogsEncryptionConfiguration"
    ]
    """<p>The encryption configuration for centralization destination log groups.</p>"""
    backup_configuration: NotRequired[
        "capo_observabilityadmin.types.logs_backup_configuration.LogsBackupConfiguration"
    ]
    """<p>Configuration defining the backup region and an optional KMS key for the backup destination.</p>"""
    log_group_name_configuration: NotRequired[
        "capo_observabilityadmin.types.log_group_name_configuration.LogGroupNameConfiguration"
    ]
    """<p>Configuration that specifies a naming pattern for destination log groups created during centralization. The pattern supports static text and dynamic variables that are replaced with source attributes when log groups are created.</p>"""
    tag_propagation_configuration: NotRequired[
        "capo_observabilityadmin.types.tag_propagation_configuration.TagPropagationConfiguration"
    ]
    """<p>Specifies the tag propagation configuration for this centralization rule. When present, <code>LogGroupNameConfiguration</code> must use a <code>LogGroupNamePattern</code> that contains <code>${source.logGroup}</code>, <code>${source.accountId}</code>, and <code>${source.region}</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationLogsConfiguration) -> dict:
    out: dict = {}
    if "logs_encryption_configuration" in value:
        import capo_observabilityadmin.types.logs_encryption_configuration

        out["LogsEncryptionConfiguration"] = (
            capo_observabilityadmin.types.logs_encryption_configuration.serialize_json(
                value["logs_encryption_configuration"]
            )
        )
    if "backup_configuration" in value:
        import capo_observabilityadmin.types.logs_backup_configuration

        out["BackupConfiguration"] = (
            capo_observabilityadmin.types.logs_backup_configuration.serialize_json(
                value["backup_configuration"]
            )
        )
    if "log_group_name_configuration" in value:
        import capo_observabilityadmin.types.log_group_name_configuration

        out["LogGroupNameConfiguration"] = (
            capo_observabilityadmin.types.log_group_name_configuration.serialize_json(
                value["log_group_name_configuration"]
            )
        )
    if "tag_propagation_configuration" in value:
        import capo_observabilityadmin.types.tag_propagation_configuration

        out["TagPropagationConfiguration"] = (
            capo_observabilityadmin.types.tag_propagation_configuration.serialize_json(
                value["tag_propagation_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DestinationLogsConfiguration:
    out: DestinationLogsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("LogsEncryptionConfiguration") is not None:
        import capo_observabilityadmin.types.logs_encryption_configuration

        out["logs_encryption_configuration"] = (
            capo_observabilityadmin.types.logs_encryption_configuration.deserialize_json(
                data["LogsEncryptionConfiguration"]
            )
        )
    if data.get("BackupConfiguration") is not None:
        import capo_observabilityadmin.types.logs_backup_configuration

        out["backup_configuration"] = (
            capo_observabilityadmin.types.logs_backup_configuration.deserialize_json(
                data["BackupConfiguration"]
            )
        )
    if data.get("LogGroupNameConfiguration") is not None:
        import capo_observabilityadmin.types.log_group_name_configuration

        out["log_group_name_configuration"] = (
            capo_observabilityadmin.types.log_group_name_configuration.deserialize_json(
                data["LogGroupNameConfiguration"]
            )
        )
    if data.get("TagPropagationConfiguration") is not None:
        import capo_observabilityadmin.types.tag_propagation_configuration

        out["tag_propagation_configuration"] = (
            capo_observabilityadmin.types.tag_propagation_configuration.deserialize_json(
                data["TagPropagationConfiguration"]
            )
        )
    return out
