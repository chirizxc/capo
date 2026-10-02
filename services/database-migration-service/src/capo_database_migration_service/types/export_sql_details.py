"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ExportSqlDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class ExportSqlDetails(TypedDict, closed=True):
    s3_object_key: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The Amazon S3 URI of the object that contains the ZIP archive with exported DDL scripts.</p>"""
    object_url: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The URL of the Amazon S3 object that contains the ZIP archive with exported DDL scripts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportSqlDetails) -> dict:
    out: dict = {}
    if "s3_object_key" in value:
        out["S3ObjectKey"] = value["s3_object_key"]
    if "object_url" in value:
        out["ObjectURL"] = value["object_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportSqlDetails:
    out: ExportSqlDetails = {}  # type: ignore[typeddict-item]
    if data.get("S3ObjectKey") is not None:
        out["s3_object_key"] = data["S3ObjectKey"]
    if data.get("ObjectURL") is not None:
        out["object_url"] = data["ObjectURL"]
    return out
