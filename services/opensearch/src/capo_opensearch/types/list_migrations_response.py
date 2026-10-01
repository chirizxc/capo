"""Generated from Smithy shape ``com.amazonaws.opensearch#ListMigrationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.migration_summary_list
    import capo_opensearch.types.string


class ListMigrationsResponse(TypedDict, closed=True):
    migrations: NotRequired[
        "capo_opensearch.types.migration_summary_list.MigrationSummaryList"
    ]
    """<p>A list of migration job summaries for the specified application.</p>"""
    next_token: NotRequired["capo_opensearch.types.string.String"]
    """<p>The pagination token to use in a subsequent call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMigrationsResponse) -> dict:
    out: dict = {}
    if "migrations" in value:
        import capo_opensearch.types.migration_summary_list

        out["migrations"] = capo_opensearch.types.migration_summary_list.serialize_json(
            value["migrations"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMigrationsResponse:
    out: ListMigrationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("migrations") is not None:
        import capo_opensearch.types.migration_summary_list

        out["migrations"] = (
            capo_opensearch.types.migration_summary_list.deserialize_json(
                data["migrations"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
