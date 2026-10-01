"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbBackupSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_backup_summary

DbBackupSummaryList: TypeAlias = list[
    "capo_timestream_influxdb.types.db_backup_summary.DbBackupSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbBackupSummaryList) -> list:
    import capo_timestream_influxdb.types.db_backup_summary

    out: list = []
    for item in value:
        out.append(
            capo_timestream_influxdb.types.db_backup_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DbBackupSummaryList:
    import capo_timestream_influxdb.types.db_backup_summary

    out: DbBackupSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_timestream_influxdb.types.db_backup_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
