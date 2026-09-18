"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#TableRestoreStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class TableRestoreStatus(TypedDict, closed=True):
    table_restore_request_id: NotRequired["str"]
    """<p>The ID of the RestoreTableFromSnapshot request.</p>"""
    status: NotRequired["str"]
    """<p>A value that describes the current state of the table restore request. Possible values are <code>SUCCEEDED</code>, <code>FAILED</code>, <code>CANCELED</code>, <code>PENDING</code>, and <code>IN_PROGRESS</code>.</p>"""
    message: NotRequired["str"]
    """<p>A message that explains the returned status. For example, if the status of the operation is <code>FAILED</code>, the message explains why the operation failed.</p>"""
    request_time: NotRequired["datetime.datetime"]
    """<p>The time that the table restore request was made, in Universal Coordinated Time (UTC).</p>"""
    namespace_name: NotRequired["str"]
    """<p>The namespace of the table being restored from.</p>"""
    workgroup_name: NotRequired["str"]
    """<p>The name of the workgroup being restored from.</p>"""
    snapshot_name: NotRequired["str"]
    """<p>The name of the snapshot being restored from.</p>"""
    progress_in_mega_bytes: NotRequired["int"]
    """<p>The amount of data restored to the new table so far, in megabytes (MB).</p>"""
    total_data_in_mega_bytes: NotRequired["int"]
    """<p>The total amount of data to restore to the new table, in megabytes (MB).</p>"""
    source_database_name: NotRequired["str"]
    """<p>The name of the source database being restored from.</p>"""
    source_schema_name: NotRequired["str"]
    """<p>The name of the source schema being restored from.</p>"""
    source_table_name: NotRequired["str"]
    """<p>The name of the source table being restored from.</p>"""
    target_database_name: NotRequired["str"]
    """<p>The name of the database to restore to.</p>"""
    target_schema_name: NotRequired["str"]
    """<p>The name of the schema to restore to.</p>"""
    new_table_name: NotRequired["str"]
    """<p>The name of the table to create from the restore operation.</p>"""
    recovery_point_id: NotRequired["str"]
    """<p>The ID of the recovery point being restored from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableRestoreStatus) -> dict:
    out: dict = {}
    if "table_restore_request_id" in value:
        out["tableRestoreRequestId"] = value["table_restore_request_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "message" in value:
        out["message"] = value["message"]
    if "request_time" in value:
        import capo_redshift_serverless.types._prelude.timestamp

        out["requestTime"] = (
            capo_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["request_time"]
            )
        )
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "workgroup_name" in value:
        out["workgroupName"] = value["workgroup_name"]
    if "snapshot_name" in value:
        out["snapshotName"] = value["snapshot_name"]
    if "progress_in_mega_bytes" in value:
        out["progressInMegaBytes"] = value["progress_in_mega_bytes"]
    if "total_data_in_mega_bytes" in value:
        out["totalDataInMegaBytes"] = value["total_data_in_mega_bytes"]
    if "source_database_name" in value:
        out["sourceDatabaseName"] = value["source_database_name"]
    if "source_schema_name" in value:
        out["sourceSchemaName"] = value["source_schema_name"]
    if "source_table_name" in value:
        out["sourceTableName"] = value["source_table_name"]
    if "target_database_name" in value:
        out["targetDatabaseName"] = value["target_database_name"]
    if "target_schema_name" in value:
        out["targetSchemaName"] = value["target_schema_name"]
    if "new_table_name" in value:
        out["newTableName"] = value["new_table_name"]
    if "recovery_point_id" in value:
        out["recoveryPointId"] = value["recovery_point_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TableRestoreStatus:
    out: TableRestoreStatus = {}  # type: ignore[typeddict-item]
    if data.get("tableRestoreRequestId") is not None:
        out["table_restore_request_id"] = data["tableRestoreRequestId"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("requestTime") is not None:
        import capo_redshift_serverless.types._prelude.timestamp

        out["request_time"] = (
            capo_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["requestTime"]
            )
        )
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    if data.get("workgroupName") is not None:
        out["workgroup_name"] = data["workgroupName"]
    if data.get("snapshotName") is not None:
        out["snapshot_name"] = data["snapshotName"]
    if data.get("progressInMegaBytes") is not None:
        out["progress_in_mega_bytes"] = data["progressInMegaBytes"]
    if data.get("totalDataInMegaBytes") is not None:
        out["total_data_in_mega_bytes"] = data["totalDataInMegaBytes"]
    if data.get("sourceDatabaseName") is not None:
        out["source_database_name"] = data["sourceDatabaseName"]
    if data.get("sourceSchemaName") is not None:
        out["source_schema_name"] = data["sourceSchemaName"]
    if data.get("sourceTableName") is not None:
        out["source_table_name"] = data["sourceTableName"]
    if data.get("targetDatabaseName") is not None:
        out["target_database_name"] = data["targetDatabaseName"]
    if data.get("targetSchemaName") is not None:
        out["target_schema_name"] = data["targetSchemaName"]
    if data.get("newTableName") is not None:
        out["new_table_name"] = data["newTableName"]
    if data.get("recoveryPointId") is not None:
        out["recovery_point_id"] = data["recoveryPointId"]
    return out
