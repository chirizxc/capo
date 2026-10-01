"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbBackupConfigurationInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_backup_configuration

DbBackupConfigurationInputList: TypeAlias = list[
    "capo_timestream_influxdb.types.db_backup_configuration.DbBackupConfiguration"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbBackupConfigurationInputList) -> list:
    import capo_timestream_influxdb.types.db_backup_configuration

    out: list = []
    for item in value:
        out.append(
            capo_timestream_influxdb.types.db_backup_configuration.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DbBackupConfigurationInputList:
    import capo_timestream_influxdb.types.db_backup_configuration

    out: DbBackupConfigurationInputList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_timestream_influxdb.types.db_backup_configuration.deserialize_aws_json_1_0(
                item
            )
        )
    return out
