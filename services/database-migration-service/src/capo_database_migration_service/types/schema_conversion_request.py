"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SchemaConversionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.error_details
    import capo_database_migration_service.types.export_sql_details
    import capo_database_migration_service.types.progress
    import capo_database_migration_service.types.string


class SchemaConversionRequest(TypedDict, closed=True):
    status: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The schema conversion operation status. Possible values:</p> <ul> <li> <p> <code>RECEIVED</code> – The operation is received but not yet queued for processing.</p> </li> <li> <p> <code>IN_PROGRESS</code> – The operation is queued or actively running.</p> </li> <li> <p> <code>SUCCESS</code> – The operation completed successfully.</p> </li> <li> <p> <code>FAILED</code> – The operation did not complete.</p> </li> <li> <p> <code>CANCELING</code> – The operation is being canceled. The operation might still succeed or fail before cancellation takes effect.</p> </li> <li> <p> <code>CANCELED</code> – The operation was canceled before completion.</p> </li> </ul>"""
    request_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The identifier for the schema conversion action.</p>"""
    migration_project_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The migration project ARN.</p>"""
    error: NotRequired[
        "capo_database_migration_service.types.error_details.ErrorDetails"
    ]
    export_sql_details: NotRequired[
        "capo_database_migration_service.types.export_sql_details.ExportSqlDetails"
    ]
    """<p>The Amazon S3 location of the ZIP archive that contains the exported data definition language (DDL) scripts.</p> <note> <p>DMS populates this field only for the <code>DescribeMetadataModelExportsAsScript</code> operation.</p> </note>"""
    progress: NotRequired["capo_database_migration_service.types.progress.Progress"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaConversionRequest) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    if "request_identifier" in value:
        out["RequestIdentifier"] = value["request_identifier"]
    if "migration_project_arn" in value:
        out["MigrationProjectArn"] = value["migration_project_arn"]
    if "error" in value:
        import capo_database_migration_service.types.error_details

        out["Error"] = (
            capo_database_migration_service.types.error_details.serialize_aws_json_1_1(
                value["error"]
            )
        )
    if "export_sql_details" in value:
        import capo_database_migration_service.types.export_sql_details

        out["ExportSqlDetails"] = (
            capo_database_migration_service.types.export_sql_details.serialize_aws_json_1_1(
                value["export_sql_details"]
            )
        )
    if "progress" in value:
        import capo_database_migration_service.types.progress

        out["Progress"] = (
            capo_database_migration_service.types.progress.serialize_aws_json_1_1(
                value["progress"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaConversionRequest:
    out: SchemaConversionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("RequestIdentifier") is not None:
        out["request_identifier"] = data["RequestIdentifier"]
    if data.get("MigrationProjectArn") is not None:
        out["migration_project_arn"] = data["MigrationProjectArn"]
    if data.get("Error") is not None:
        import capo_database_migration_service.types.error_details

        out["error"] = (
            capo_database_migration_service.types.error_details.deserialize_aws_json_1_1(
                data["Error"]
            )
        )
    if data.get("ExportSqlDetails") is not None:
        import capo_database_migration_service.types.export_sql_details

        out["export_sql_details"] = (
            capo_database_migration_service.types.export_sql_details.deserialize_aws_json_1_1(
                data["ExportSqlDetails"]
            )
        )
    if data.get("Progress") is not None:
        import capo_database_migration_service.types.progress

        out["progress"] = (
            capo_database_migration_service.types.progress.deserialize_aws_json_1_1(
                data["Progress"]
            )
        )
    return out
