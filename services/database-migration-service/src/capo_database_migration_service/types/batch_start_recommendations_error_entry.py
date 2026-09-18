"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#BatchStartRecommendationsErrorEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class BatchStartRecommendationsErrorEntry(TypedDict, closed=True):
    database_id: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The identifier of the source database.</p>"""
    message: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The information about the error.</p>"""
    code: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The code of an error that occurred during the analysis of the source database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchStartRecommendationsErrorEntry) -> dict:
    out: dict = {}
    if "database_id" in value:
        out["DatabaseId"] = value["database_id"]
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchStartRecommendationsErrorEntry:
    out: BatchStartRecommendationsErrorEntry = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseId") is not None:
        out["database_id"] = data["DatabaseId"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    return out
