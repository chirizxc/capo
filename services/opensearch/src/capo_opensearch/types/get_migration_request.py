"""Generated from Smithy shape ``com.amazonaws.opensearch#GetMigrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.string


class GetMigrationRequest(TypedDict, closed=True):
    migration_id: "capo_opensearch.types.string.String"
    """<p>The unique identifier of the migration job to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMigrationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMigrationRequest:
    out: GetMigrationRequest = {}  # type: ignore[typeddict-item]
    return out
