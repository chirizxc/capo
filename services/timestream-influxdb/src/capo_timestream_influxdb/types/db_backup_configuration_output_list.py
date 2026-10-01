"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbBackupConfigurationOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_backup_configuration_output

DbBackupConfigurationOutputList: TypeAlias = list[
    "capo_timestream_influxdb.types.db_backup_configuration_output.DbBackupConfigurationOutput"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbBackupConfigurationOutputList) -> list:
    import capo_timestream_influxdb.types.db_backup_configuration_output

    out: list = []
    for item in value:
        out.append(
            capo_timestream_influxdb.types.db_backup_configuration_output.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DbBackupConfigurationOutputList:
    import capo_timestream_influxdb.types.db_backup_configuration_output

    out: DbBackupConfigurationOutputList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_timestream_influxdb.types.db_backup_configuration_output.deserialize_aws_json_1_0(
                item
            )
        )
    return out
