"""Generated from Smithy shape ``com.amazonaws.opensearch#GetMigrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.application_id
    import capo_opensearch.types.integer
    import capo_opensearch.types.migration_error
    import capo_opensearch.types.migration_source
    import capo_opensearch.types.string
    import capo_opensearch.types.update_timestamp


class GetMigrationResponse(TypedDict, closed=True):
    migration_id: NotRequired["capo_opensearch.types.string.String"]
    """<p>The unique identifier of the migration job.</p>"""
    status: NotRequired["capo_opensearch.types.string.String"]
    """<p>The current status of the migration job. Valid values are <code>PENDING</code>, <code>IN_PROGRESS</code>, <code>SUCCEEDED</code>, and <code>FAILED</code>.</p>"""
    application_id: NotRequired["capo_opensearch.types.application_id.ApplicationId"]
    """<p>The unique identifier of the OpenSearch application associated with the migration.</p>"""
    source: NotRequired["capo_opensearch.types.migration_source.MigrationSource"]
    """<p>The source configuration for the migration, including the data source ARN.</p>"""
    exported_count: "capo_opensearch.types.integer.Integer"
    """<p>The number of saved objects exported from the source data source.</p>"""
    imported_count: "capo_opensearch.types.integer.Integer"
    """<p>The number of saved objects successfully imported into the target workspace.</p>"""
    error: NotRequired["capo_opensearch.types.migration_error.MigrationError"]
    """<p>Error details if the migration failed or completed with errors.</p>"""
    created_at: NotRequired["capo_opensearch.types.update_timestamp.UpdateTimestamp"]
    """<p>The date and time when the migration job was created.</p>"""
    updated_at: NotRequired["capo_opensearch.types.update_timestamp.UpdateTimestamp"]
    """<p>The date and time when the migration job was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMigrationResponse) -> dict:
    out: dict = {}
    if "migration_id" in value:
        out["migrationId"] = value["migration_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "source" in value:
        import capo_opensearch.types.migration_source

        out["source"] = capo_opensearch.types.migration_source.serialize_json(
            value["source"]
        )
    out["exportedCount"] = value.get("exported_count", 0)
    out["importedCount"] = value.get("imported_count", 0)
    if "error" in value:
        import capo_opensearch.types.migration_error

        out["error"] = capo_opensearch.types.migration_error.serialize_json(
            value["error"]
        )
    if "created_at" in value:
        import capo_opensearch.types.update_timestamp

        out["createdAt"] = capo_opensearch.types.update_timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_opensearch.types.update_timestamp

        out["updatedAt"] = capo_opensearch.types.update_timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetMigrationResponse:
    out: GetMigrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("migrationId") is not None:
        out["migration_id"] = data["migrationId"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    if data.get("source") is not None:
        import capo_opensearch.types.migration_source

        out["source"] = capo_opensearch.types.migration_source.deserialize_json(
            data["source"]
        )
    if data.get("exportedCount") is not None:
        out["exported_count"] = data["exportedCount"]
    else:
        out["exported_count"] = 0
    if data.get("importedCount") is not None:
        out["imported_count"] = data["importedCount"]
    else:
        out["imported_count"] = 0
    if data.get("error") is not None:
        import capo_opensearch.types.migration_error

        out["error"] = capo_opensearch.types.migration_error.deserialize_json(
            data["error"]
        )
    if data.get("createdAt") is not None:
        import capo_opensearch.types.update_timestamp

        out["created_at"] = capo_opensearch.types.update_timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_opensearch.types.update_timestamp

        out["updated_at"] = capo_opensearch.types.update_timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
