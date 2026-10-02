"""Generated from Smithy shape ``com.amazonaws.opensearch#StartMigrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.string


class StartMigrationResponse(TypedDict, closed=True):
    migration_id: NotRequired["capo_opensearch.types.string.String"]
    """<p>The unique identifier of the migration job.</p>"""
    status: NotRequired["capo_opensearch.types.string.String"]
    """<p>The initial status of the migration job. The status is <code>PENDING</code> when a migration is first created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMigrationResponse) -> dict:
    out: dict = {}
    if "migration_id" in value:
        out["migrationId"] = value["migration_id"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> StartMigrationResponse:
    out: StartMigrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("migrationId") is not None:
        out["migration_id"] = data["migrationId"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
